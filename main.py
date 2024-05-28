import os
import shutil

def organize_files(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Ignore directories and hidden files
        if os.path.isfile(os.path.join(directory, filename)) and not filename.startswith('.'):
            # Get the file extension
            file_extension = filename.split('.')[-1]
            
            # Create a directory for the file extension if it doesn't exist
            if not os.path.exists(os.path.join(directory, file_extension)):
                os.makedirs(os.path.join(directory, file_extension))
            
            # Move the file to the corresponding directory
            shutil.move(os.path.join(directory, filename), os.path.join(directory, file_extension, filename))
            print(f"Moved {filename} to {file_extension} folder")

if __name__ == "__main__":
    directory_to_organize = r"/path/to/your/directory"
    organize_files(directory_to_organize)
