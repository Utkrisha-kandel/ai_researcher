from langchain_core.tools import tool
import io
import requests

@tool
def read_pdf(url: str) -> str:
    """Read and extract text from a PDF file given its URL.

    Args:
        url: The URL of the PDF file to read

    Returns:
        The extracted text content from the PDF
    """
    try:
        print(f"Fetching PDF from: {url}")
        response = requests.get(url, timeout=30)  # ← timeout added
        
        if not response.ok:
            return f"Failed to fetch PDF: HTTP {response.status_code} from {url}"

        # Use pypdf instead of deprecated PyPDF2
        try:
            from pypdf import PdfReader
        except ImportError:
            from PyPDF2 import PdfReader

        pdf_file = io.BytesIO(response.content)
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        print(f"Extracting text from {num_pages} pages...")
        text = ""
        for i, page in enumerate(pdf_reader.pages, 1):
            print(f"  Page {i}/{num_pages}")
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        if not text.strip():
            return "No text could be extracted from this PDF (may be scanned/image-based)."

        extracted = text.strip()
        print(f"Successfully extracted {len(extracted)} characters")

        # Truncate to avoid flooding the agent's context window
        if len(extracted) > 8000:
            extracted = extracted[:8000] + "\n\n[... truncated for context window ...]"

        return extracted

    except Exception as e:
        print(f"Error reading PDF: {str(e)}")
        return f"Error reading PDF from {url}: {str(e)}"  # ← always return a string