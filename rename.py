import os

# Specify the directory containing the images
folder_path = 'data'  # Replace with the path to your images folder

# Get a list of all files in the directory
files = os.listdir(folder_path)

# Initialize a counter for numbering
counter = 1

for file in files:
    # Get the file extension
    file_extension = os.path.splitext(file)[1]
    
    # Format the new file name with leading zeros (5 digits)
    new_name = f"{counter:05}{file_extension}"
    
    # Create the full path for the old and new file names
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(old_file_path, new_file_path)
    print(f"Renamed '{file}' to '{new_name}'")

    # Increment the counter
    counter += 1
