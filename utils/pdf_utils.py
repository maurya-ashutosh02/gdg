from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(uploaded_file):
    if not uploaded_file:
        return ""
    file_bytes = uploaded_file.read()
    reader = PdfReader(io.BytesIO(file_bytes))
    text = []
    for page in reader.pages:
        try:
            text.append(page.extract_text() or "")
        except Exception:
            text.append("")
    return "\n".join(text)
