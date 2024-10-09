from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_images_to_pdf(folder_path, output_pdf_prefix):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    if not image_files:
        print("No image files found in the folder.")
        return

    total_files = len(image_files)
    num_pdfs = 6  # Number of PDFs to create

    files_per_pdf = total_files // num_pdfs
    remainder = total_files % num_pdfs

    start_index = 0

    for pdf_index in range(1, num_pdfs + 1):
        num_files_in_pdf = files_per_pdf
        if remainder > 0:
            num_files_in_pdf += 1
            remainder -= 1

        pdf_name = f"{output_pdf_prefix}_{pdf_index}.pdf"

        c = canvas.Canvas(pdf_name, pagesize=letter)

        for i in range(start_index, start_index + num_files_in_pdf):
            image_file = image_files[i]
            image_path = os.path.join(folder_path, image_file)
            img = Image.open(image_path)
            img_width, img_height = img.size

            c.setPageSize((img_width, img_height))
            c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
            c.showPage()

        c.save()

        start_index += num_files_in_pdf

    print(f"{total_files} images split into {num_pdfs} PDFs and saved as '{output_pdf_prefix}_1.pdf', '{output_pdf_prefix}_2.pdf', etc.")

if __name__ == "__main__":
    input_folder = "certificados"
    output_pdf_prefix = "output"
    convert_images_to_pdf(input_folder, output_pdf_prefix)