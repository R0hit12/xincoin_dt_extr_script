import os
import PyPDF2

def save_pdf_pages_to_text(file_path, output_folder):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page_num, page in enumerate(pdf_reader.pages, start=1):
            content = page.extract_text()
            output_file_path = os.path.join(output_folder, f'page_{page_num}.txt')
            with open(output_file_path, 'w') as output_file:
                output_file.write(content)
