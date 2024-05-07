# the folder contains 44 text files named as: Int3-2-44.txt, Int3-2-43.txt, Int3-2-42.txt...
# the goal is to rename the files as: Int1-2-44.txt, Int1-2-43.txt, Int1-2-42.txt...



import os

# Define the directory
dir_path = r'C:\Users\...'  # replace with your directory path

# Get list of all files
files = os.listdir(dir_path)

# Iterate over each file
for file in files:
    # Check if the file starts with 'Int3'
    if file.startswith('aaa'):
        # Construct new filename
        new_filename = file.replace('aaa', '')
        
        # Get full file paths
        old_file_path = os.path.join(dir_path, file)
        new_file_path = os.path.join(dir_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)