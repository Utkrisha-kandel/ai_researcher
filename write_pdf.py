#Step1: Install tectonic and Import dependencies
from langchain_core.tools import tool
from datetime import datetime
from pathlib import Path
import subprocess
import shutil
#STep2: Create a directory
def render_latex_pdf(latex_content:str)->str:
    """Render a LaTeX document to PDF,
    Args:
        latex_content:The LaTeX document content as a string
    Returns:
        Path to the generated PDF document
    
    """
    tectonic_path = shutil.which("tectonic") or r"C:\Users\ecs\AppData\Local\Programs\tectonic\tectonic.exe"

    if  tectonic_path is None:
        raise RuntimeError(
            "tectonic is not installed. Install it first on your system"
        )
    try:
            output_dir = Path("output").absolute()
            output_dir.mkdir(exist_ok=True)
            #step3: Setup filenames
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            tex_filename = f"paper_{timestamp}.tex"
            pdf_filename = f"paper_{timestamp}.pdf"
            #step4: Export as tex and pdf
            tex_file = output_dir/tex_filename
            tex_file.write_text(latex_content)

            result = subprocess.run(
                [tectonic_path,tex_filename,"--outdir",str(output_dir)],
                cwd=output_dir,
                capture_output=True,
                text=True
            )
            final_pdf = output_dir / pdf_filename
            if not final_pdf.exists():
                raise FileNotFoundError("PDF file was not generated")
    except Exception as e:
         print(f"Error rending LaTeX: {str(e)}")
         raise
# sample_latex = r"""
# \documentclass{article}

# \usepackage{amsmath} % for math symbols

# \title{My First LaTeX Document}
# \author{Your Name}
# \date{\today}

# \begin{document}

# \maketitle

# \section{Introduction}
# This is my first document written in \LaTeX.  
# LaTeX is great for writing scientific papers, reports, and even books.

# \section{Math Example}
# Here is Einstein's famous equation:

# \[
# E = mc^2
# \]

# We can also write inline math like this: $a^2 + b^2 = c^2$.

# \section{Conclusion}
# With Tectonic, building LaTeX into PDF is as easy as:
# \begin{verbatim}
# tectonic sample.tex
# \end{verbatim}

# \end{document}



# """
# render_latex_pdf(sample_latex)