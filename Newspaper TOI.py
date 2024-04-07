import os
import re
import boto3
from pdf2image import convert_from_path
# import shutil

def extract_text_from_image(image_path):
    textract_client = boto3.client('textract', region_name='ap-south-1')
    with open(image_path, 'rb') as file:
        response = textract_client.analyze_document(Document={'Bytes': file.read()}, FeatureTypes=['TABLES', 'FORMS'])

    extracted_text = ""
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + "\n"

    return extracted_text

def extract_page_number_year_from_text(text):
    lines = text.split('\n')
    page_number = lines[0].strip()
    state = lines[2].strip()
    state = state.replace("_", " ").replace("THE ", "").strip()
    date = re.search(r'[A-Za-z]+, ([A-Za-z]+ \d{1,2})-(\d{4})', lines[3])
    year = date.group(2) if date else ""
    return page_number, state, year

def extract_text_from_image_folder(folder_path):
    raw_folder = os.path.join(folder_path, 'raw')
    image_folder = os.path.join(folder_path, 'image')
    os.makedirs(raw_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)
    processed_files = set()  # To keep track of processed files
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith((".jpg", ".jpeg", ".png")) and file_name not in processed_files:
                image_path = os.path.join(root, file_name)
                print("Extracting text from image:", image_path)  # Debug statement
                extracted_text = extract_text_from_image(image_path)

                # Extracting dynamic prefix from PDF filename
                pdf_name = os.path.splitext(file_name)[0]
                prefix_parts = pdf_name.split("_")
                prefix = "_".join(prefix_parts[:-3]) + "-" + "_".join(prefix_parts[-3:-2])

                page_number, state, year = extract_page_number_year_from_text(extracted_text)

                prefix = prefix.replace(".pdf", "")
                page_number = page_number.replace("_", "-")
                state  = state.replace("TIMES_OF_INDIA.", "").replace(" _", "")
                state  = state.replace("TIMES_OF_INDIA,_","")
                state  = state.replace("TIMES OF INDIA,","")

                output_file_name = f"{prefix}_{year}_{state}_{page_number}.txt"
                output_path = os.path.join(raw_folder, output_file_name)

                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(extracted_text)

                print("Text extraction complete for:", image_path)
                print("Text saved to:", output_path)

                # Rename image file
                new_image_name = os.path.splitext(output_file_name)[0] + ".jpg"
                os.rename(image_path, os.path.join(image_folder, new_image_name))

                # Add the processed file to the set
                processed_files.add(file_name)

    # Rename PDF files in the PDF folder
    pdf_folder = os.path.join(folder_path, 'pdf')
    for root, dirs, files in os.walk(pdf_folder):
        for file_name in files:
            if file_name.endswith(".pdf"):
                # Remove "_page_1.pdf" from the file name
                prefix = os.path.splitext(file_name)[0].rsplit('_page_1', 1)[0]
                new_pdf_name = f"{prefix}.pdf"
                os.rename(os.path.join(pdf_folder, file_name), os.path.join(pdf_folder, new_pdf_name))

def convert_pdf_to_images(pdf_folder, output_folder, poppler_path):
    image_folder = os.path.join(output_folder, 'image')
    os.makedirs(image_folder, exist_ok=True)
    for root, dirs, files in os.walk(pdf_folder):
        for file_name in files:
            if file_name.endswith(".pdf"):
                pdf_file_path = os.path.join(root, file_name)
                print("Converting PDF to images:", pdf_file_path)  # Debug statement
                images = convert_from_path(pdf_file_path, poppler_path=poppler_path)
                for i, image in enumerate(images):
                    image_path = os.path.join(image_folder, f"{file_name}_page_{i+1}.jpg") 
                    image.save(image_path, 'JPEG')  
                    print(f"Page {i+1} of {file_name} saved as {image_path}")
                
                print(f"Images converted for {file_name}")

    # Rename PDF files in the PDF folder
    for root, dirs, files in os.walk(pdf_folder):
        for file_name in files:
            if file_name.endswith(".pdf"):
                old_pdf_path = os.path.join(root, file_name)
                new_pdf_name = re.sub(r'(\d{2})_(\d{2})', r'\1-\2', file_name)
                new_pdf_name = re.sub(r'_page_1.pdf', '', new_pdf_name)
                new_pdf_name = f"{new_pdf_name[:-4]}_{state}_{page_number}.pdf"
                new_pdf_path = os.path.join(root, new_pdf_name)
                print(f"Renaming: {old_pdf_path} -> {new_pdf_path}")
                os.rename(old_pdf_path, new_pdf_path)

if __name__ == "__main__":
    # Replace these with your AWS credentials and region if needed
    os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAUG5QZ7LXJU3FHLST'
    os.environ['AWS_SECRET_ACCESS_KEY'] = '/pLoHq1Dc5ZEOQn6+yvZyepX995mujdBCxa0OxXP'
    os.environ['AWS_DEFAULT_REGION'] = 'ap-south-1'  

    pdf_folder = r"C:\Users\Ganesh.Kc\Desktop\Newspaper\pdf"
    output_folder = r"C:\Users\Ganesh.Kc\Desktop\Newspaper"
    poppler_path = r"C:\Program Files\poppler-24.02.0\Library\bin"

    convert_pdf_to_images(pdf_folder, output_folder, poppler_path)
    extract_text_from_image_folder(output_folder)
