import os
import pytesseract
from PyPDF2 import PdfReader
from PIL import Image
from docx import Document
import pandas as pd

# Optional: used for PDF OCR
try:
    from pdf2image import convert_from_path
    has_pdf2image = True
except ImportError:
    has_pdf2image = False

# Path
path = '/home/prit/Desktop/django-projects/TextWrapper/python-practice-2025'
output_file = 'staticname.txt'

# Extensions
image_exts = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
text_exts = ['.txt', '.py', '.csv', '.md', '.html']
unsupported_exts = ['.zip', '.exe', '.dll', '.doc']  # add more if needed

# ---- Extraction functions ----
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            text = ''
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        if not text.strip() and has_pdf2image:
            return extract_text_from_pdf_ocr(file_path)
        elif not text.strip():
            return "[VALIDATION ERROR: PDF is scanned and pdf2image not installed]"
        return text
    except Exception:
        return "[VALIDATION ERROR: Cannot extract text from PDF]"

def extract_text_from_pdf_ocr(file_path):
    try:
        images = convert_from_path(file_path)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text
    except Exception:
        return "[VALIDATION ERROR: OCR failed for scanned PDF]"

def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    except Exception:
        return "[VALIDATION ERROR: Cannot extract text from Word file]"

def extract_text_from_excel(file_path):
    try:
        df_list = pd.read_excel(file_path, sheet_name=None)
        output = ""
        for sheet, df in df_list.items():
            output += f"[Sheet: {sheet}]\n"
            output += df.to_string(index=False)
            output += "\n\n"
        return output
    except Exception:
        return "[VALIDATION ERROR: Cannot extract text from Excel file]"

def extract_text_from_image(file_path):
    try:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
    except Exception:
        return "[VALIDATION ERROR: Cannot extract text from image]"

def extract_text_from_plain_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return "[VALIDATION ERROR: Cannot read plain text file]"

# ---- Main Script ----
with open(output_file, 'w', encoding='utf-8') as outfile:
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()

            outfile.write(f"\n== {file} ==\n")

            if ext in unsupported_exts:
                content = "[VALIDATION ERROR: File type not supported]"

            elif ext in text_exts:
                content = extract_text_from_plain_text(file_path)

            elif ext == '.pdf':
                content = extract_text_from_pdf(file_path)

            elif ext == '.docx':
                content = extract_text_from_docx(file_path)

            elif ext == '.xlsx':
                content = extract_text_from_excel(file_path)

            elif ext in image_exts:
                content = extract_text_from_image(file_path)

            else:
                content = "[VALIDATION ERROR: Unknown or unsupported file type]"

            outfile.write(content + "\n\n")


'''
---

### **📁 Project: TextWrapper – Multi-format Text Extraction Tool**

**Technologies:** Python, PyPDF2, python-docx, pandas, PIL, pytesseract, pdf2image

Developed a Python-based tool to solve the real-world problem of extracting and unifying text from folders containing mixed file types (PDFs, Word docs, Excel sheets, images, plain text). The tool uses:

* **PyPDF2** to extract text from digital PDF files.
* **python-docx** to parse text from `.docx` Word documents.
* **pandas** to read and convert Excel `.xlsx` data into string format.
* **PIL (Pillow)** to handle image files and prepare them for OCR.
* **pytesseract + pdf2image** to extract text from scanned PDFs and images using OCR.

The tool validates file types, handles errors gracefully, and consolidates all readable content into a single output file.

---

✅ **You can copy this directly to your CV under the “Projects” section.** Let me know if you want a version tailored for **GitHub**, **LinkedIn**, or **portfolio websites**.



'''
