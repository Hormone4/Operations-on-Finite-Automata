import os

# Define the directory
dir_path = r'C:\Users\...'  # replace with your directory path

# Get list of all files
files = os.listdir(dir_path)

# Iterate over each file
for file in files:
    # Check if the file starts with 'aaa'
    if file.startswith('aaa'):
        # Construct new filename
        new_filename = file.replace('aaa', '')
        
        # Get full file paths
        old_file_path = os.path.join(dir_path, file)
        new_file_path = os.path.join(dir_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)