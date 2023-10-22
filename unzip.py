import os
import zipfile

# Specify the directory where the zip file is located
folder_path = r'C:\Users\ASUS\Desktop\projects\Ack\auto-color adjusting\test\test 2\input_folder'

# List all files in the folder
files = os.listdir(folder_path)

# Filter for files with the .zip extension
zip_files = [file for file in files if file.endswith('.zip')]

if len(zip_files) == 1:
    # Assuming there is only one zip file in the folder
    zip_file_name = zip_files[0]
    
    # Create a ZipFile object and extract its contents
    with zipfile.ZipFile(os.path.join(folder_path, zip_file_name), 'r') as zip_ref:
        zip_ref.extractall(folder_path)

    print(f"Extracted '{zip_file_name}' to '{folder_path}'")
else:
    print("No zip file found or multiple zip files found in the folder.")
