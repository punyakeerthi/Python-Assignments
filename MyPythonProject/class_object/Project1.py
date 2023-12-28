'''
Created on Dec 22, 2023

@author: PBL
'''
import os
import PyPDF2

def read_pdf_and_write_to_text(pdf_path, output_text_path):
    try:
        # Check if the content folder exists, create it if not
        content_folder = '/content'
        if not os.path.exists(content_folder):
            os.makedirs(content_folder)

        # Check if the PDF file exists in the content folder
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"The PDF file '{pdf_path}' does not exist.")

        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Check if the PDF file is not encrypted
            if pdf_reader.is_encrypted:
                raise Exception("The PDF file is encrypted and cannot be processed.")

            # Read the content of each page
            text_content = ''
            print(len(pdf_reader.pages))
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text_content += page.extract_text()

        # Check if the output text file is writable
        if not os.access(content_folder, os.W_OK):
            raise PermissionError(f"Cannot write to the '{content_folder}' folder.")

        # Write the content to the output text file
        with open(output_text_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text_content)

        print(f"Successfully read the PDF file and wrote the content to '{output_text_path}'.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
pdf_path = 'D:/Data/SBM.pdf'  # Update with your PDF file path
output_text_path = 'D:/Data/output.txt'

read_pdf_and_write_to_text(pdf_path, output_text_path)
