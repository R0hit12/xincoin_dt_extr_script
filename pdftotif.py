from pdf2image import convert_from_path

def convert_pdf_to_tif(pdf_path, output_dir):
    images = convert_from_path(pdf_path)
    
    for i, image in enumerate(images):
        image_path = f"{output_dir}/page_{i+1}.tif"
        image.save(image_path, "TIFF")
        print(f"Page {i+1} converted to {image_path}")

pdf_path = "input\file1.pdf"
output_dir = "output"
convert_pdf_to_tif(pdf_path, output_dir)
