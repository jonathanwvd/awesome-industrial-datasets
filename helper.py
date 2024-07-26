import os

def rename_files_in_directory(directory):
    # List all files in the given directory
    for filename in os.listdir(directory):
        if filename.endswith('.json') or filename.endswith('.md'):
            # Create the new filename
            new_filename = filename.replace(' ', '_').lower()
            # Construct full file paths
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")

# Specify the paths to the directories containing JSON and Markdown files
json_directory = 'dataset_docs'
md_directory = 'dataset_docs/md_docs'

# Rename files in both directories
rename_files_in_directory(json_directory)
rename_files_in_directory(md_directory)

print("All files have been renamed.")
