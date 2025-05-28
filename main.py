import os
import fitz  # for PDFs
from docx import Document  # for DOCX

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

if __name__ == "__main__":
    file_path = "samples/test.pdf"  
    extracted = extract_text(file_path)
    print("=== Extracted Text ===")
    print(extracted[:1000])  # show first part
