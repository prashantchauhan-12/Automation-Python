import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# STRATEGY: PDF Manipulation
# "Can you write a script to merge these 100 contracts into one file?"
# This uses 'PyPDF2' to merge multiple PDFs and add a watermark.
# Concepts: Stream IO, Binary File Handling, Libraries.

def create_dummy_pdfs():
    from reportlab.pdfgen import canvas
    print("Generating dummy PDFs...")
    for i in range(1, 4):
        c = canvas.Canvas(f"report_{i}.pdf")
        c.drawString(100, 750, f"This is Page {i}")
        c.save()

def merge_pdfs(output_filename="merged_output.pdf"):
    print("Merging PDFs...")
    merger = PdfMerger()
    
    # Find all pdfs starting with 'report_'
    pdf_files = [f for f in os.listdir('.') if f.startswith('report_') and f.endswith('.pdf')]
    pdf_files.sort()
    
    if not pdf_files:
        print("No report_*.pdf files found!")
        return

    for pdf in pdf_files:
        print(f"Adding {pdf}...")
        merger.append(pdf)
    
    merger.write(output_filename)
    merger.close()
    print(f"Successfully merged into {output_filename}")

def add_password(input_file, output_file, password):
    print(f"Encrypting {input_file}...")
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"Encrypted file saved as {output_file}")

if __name__ == "__main__":
    # Requirement: pip install PyPDF2 reportlab
    
    # helper to make files if they don't exist
    if not os.path.exists("report_1.pdf"):
        create_dummy_pdfs()
    
    # 1. Merge
    merge_pdfs()
    
    # 2. Security (Bonus)
    add_password("merged_output.pdf", "secure_merged.pdf", "mysecretpass")
