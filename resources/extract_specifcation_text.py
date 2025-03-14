# Python script to extract the specification text from the PDF files

import os
import PyPDF2

def extract_text_from_pdfs(directory, output_directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            output_path = os.path.join(output_directory, filename.replace('.pdf', '.txt'))
            save_text_to_file(output_path, text)

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
    except Exception as e:
        print(f"Failed to extract text from {pdf_path}: {e}")
    return text

def save_text_to_file(pdf_path, text):
    text_filename = os.path.splitext(pdf_path)[0] + '.txt'
    try:
        with open(text_filename, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        print(f"Text extracted and saved to {text_filename}")
    except Exception as e:
        print(f"Failed to save text to {text_filename}: {e}")

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_directory, "specifications")
    print(f"Extracting text from PDFs in {directory}")
    output_directory = os.path.join(directory, 'output')
    print(f"Output will be saved to {output_directory}")
    extract_text_from_pdfs(directory, output_directory)
