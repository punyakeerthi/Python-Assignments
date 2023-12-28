'''
Created on Dec 22, 2023

@author: PBL
'''
import os
import PyPDF2
import shutil


def process_pdf(folder_path, output_file_path):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                   
                    if file.endswith(".pdf"):
                       
                        pdf_path = os.path.join(root, file)
                        print(f"{file} in path {pdf_path} reading started")
                         
                        try:
                            with open(pdf_path, 'rb') as pdf_file:
                                pdf_reader = PyPDF2.PdfReader(pdf_file)
                                for page_num in range(len(pdf_reader.pages)):
                                   
                                    page = pdf_reader.pages[page_num]
                                    output_file.write(page.extract_text())
                                    
                                     
                        except Exception as pdf_error:
                            print(f"Error reading PDF file '{pdf_path}': {pdf_error}")
                print(f"writing to output.txt completed")
    except Exception as output_error:
        print(f"Error writing to output file '{output_file_path}': {output_error}")

def main():
    base_folder = 'D:/Data'
    subfolders = ['One', 'Two', 'Three']
    file_name = 'LearnJava.pdf'
    

    for subfolder in subfolders:
        folder_path = os.path.join(base_folder, subfolder) 
        print(folder_path)
        for subfoldersub in subfolders:
            folder_path = os.path.join(folder_path, subfoldersub) 
            print(folder_path)
            output_file_path = os.path.join(folder_path, 'output.txt')

            try:

                os.makedirs(folder_path, exist_ok=True)
                source_path = f'{base_folder}/{file_name}'
                destination_path = f'{folder_path}/{file_name}'
                print(f'copy {file_name} file to {folder_path}')
                shutil.copy(source_path, destination_path)
               
                process_pdf(folder_path, output_file_path)
            except Exception as folder_error:
                print(f"Error processing folder '{folder_path}': {folder_error}")

if __name__ == "__main__":
    main()
