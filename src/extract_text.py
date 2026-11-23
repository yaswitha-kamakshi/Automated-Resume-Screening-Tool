import pdfplumber
from docx import Document


def extract_text(file_path):

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

    elif file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif file_path.endswith(".docx"):
        document = Document(file_path)
        text = "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

    else:
        raise ValueError("Unsupported file format")

    return text