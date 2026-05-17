import requests
import xml.etree.ElementTree as ET
from langchain.tools import tool

def search_arxiv_papers(topic: str, max_results: int = 5) -> dict:
    query = "+".join(topic.lower().split())
    for char in list('()"" '):
        if char in query:
            raise ValueError(f"Cannot have character:'{char}' in query:{query}")
    
    url = (
        "http://export.arxiv.org/api/query"
        f"?search_query=all:{query}"
        f"&max_results={max_results}"
        "&sortBy=submittedDate"
        "&sortOrder=descending"
    )

    print(f"Making request to arXiv API: {url}")
    resp = requests.get(url)
    if not resp.ok:
        raise ValueError(f"Bad response from arXiv API:{resp.status_code}\n{resp.text}")
    
    return parse_arxiv_xml(resp.text)


def parse_arxiv_xml(xml_content: str) -> dict:
    entries = []
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom"
    }
    root = ET.fromstring(xml_content)

    for entry in root.findall("atom:entry", ns):
        authors = [
            author.findtext("atom:name", namespaces=ns)
            for author in entry.findall("atom:author", ns)
        ]
        categories = [
            cat.attrib.get("term")
            for cat in entry.findall("atom:category", ns)
        ]
        pdf_link = None
        for link in entry.findall("atom:link", ns):
            if link.attrib.get("type") == "application/pdf":
                pdf_link = link.attrib.get("href")
                break

        entries.append({
            "title": entry.findtext("atom:title", namespaces=ns),
            "summary": entry.findtext("atom:summary", namespaces=ns).strip(),
            "authors": authors,
            "categories": categories,
            "pdf": pdf_link
        })

    return {"entries": entries}


@tool
def arxiv_search(topic: str) -> str:  # ← str, not list[dict]
    """Search for recently uploaded arXiv papers.

    Args:
        topic: The topic to search for papers about

    Returns:
        Formatted string of papers with title, authors, summary, and PDF link
    """
    print("ARXIV agent called")
    print(f"Searching arXiv for papers about: {topic}")
    
    papers = search_arxiv_papers(topic)
    entries = papers.get("entries", [])
    
    if not entries:
        return f"No papers found for topic: {topic}"

    # ↓ Format as readable string for the agent
    output = f"Found {len(entries)} papers about '{topic}':\n\n"
    for i, paper in enumerate(entries, 1):
        authors = ", ".join(paper["authors"][:3])  # First 3 authors
        if len(paper["authors"]) > 3:
            authors += " et al."
        output += f"""Paper {i}:
Title: {paper['title'].strip()}
Authors: {authors}
Categories: {', '.join(paper['categories'])}
PDF: {paper['pdf']}
Summary: {paper['summary'][:400]}...

"""
    return output[:4000]  # Safety truncation for context window