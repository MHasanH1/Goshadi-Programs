import os
from docx2pdf import convert
import win32com.client as win32

def convert_doc_to_pdf(doc_path, pdf_path):
    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(doc_path)
    doc.SaveAs(pdf_path, FileFormat=17)  # 17 corresponds to the PDF format
    doc.Close()
    word.Quit()

root = "D:\Programming\Code\Goshadi\watermark"
entries = os.listdir(root)
for entry in entries:
  docx_path = root + '\\' + entry
  doc_path = root + '\\' + entry
  pdf_path = root + '\\' + entry.split('.')[0] + ".pdf"
  if (entry.endswith("docx")):
    try:
      convert(docx_path, pdf_path)
    except:
      continue
  elif (entry.endswith("doc")):
    try:
      convert_doc_to_pdf(doc_path, pdf_path)
    except:
      continue
    