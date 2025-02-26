import os
import datetime

# Function to rename files in a folder
def rename_files(directory, prefix='', suffix='', add_date=False):
    # Get the current date for date-based naming
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Loop through the files in the directory
    for filename in os.listdir(directory):
        # Get the full path of the file
        file_path = os.path.join(directory, filename)

        # Skip if it's not a file
        if not os.path.isfile(file_path):
            continue

        # Get the file extension
        file_name, file_extension = os.path.splitext(filename)

        # New file name logic
        new_name = file_name

        # Add prefix if provided
        if prefix:
            new_name = prefix + new_name

        # Add suffix if provided
        if suffix:
            new_name = new_name + suffix

        # Add current date to filename if option is enabled
        if add_date:
            new_name = current_date + '_' + new_name

        # Combine the new name with the file extension
        new_file_path = os.path.join(directory, new_name + file_extension)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_name + file_extension}')

# Example Usage
directory = r'path_to_your_folder'  # Replace with the path to your folder
prefix = 'new_'  # Prefix to add (leave empty for none)
suffix = '_backup'  # Suffix to add (leave empty for none)
add_date = True  # Whether to add the current date to filenames

rename_files(directory, prefix, suffix, add_date)
