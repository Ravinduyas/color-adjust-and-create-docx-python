import os

# Specify the input folder path
input_folder = r'C:\Users\ASUS\Desktop\projects\Ack\auto-color adjusting\test\test 2\input_folder'

# Function to rename files in the input folder
def rename_files(folder):
    for i, filename in enumerate(os.listdir(folder)):
        if filename.endswith(".jpeg"):  # You can change the extension to match the file type you want to rename
            new_name = f"image_{i + 1}.jpeg"  # You can create a new naming pattern as needed
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

rename_files(input_folder)
