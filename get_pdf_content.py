import PyPDF2

def get_pdf_content(file_path):
    content = ""
    
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page in pdf_reader.pages:
            content += page.extract_text()
    
    return content

pdf_file_path = "input/file1.pdf"
pdf_content = get_pdf_content(pdf_file_path)
print(pdf_content)