import os

def rename_files(folder_path, prefix="renamed_", start_number=1):
    """
    Rename all files in the specified folder.
    :param folder_path: Path to the folder containing files
    :param prefix: Prefix for renamed files
    :param start_number: Starting number for renamed files
    """
    try:
        files = os.listdir(folder_path)
        files.sort()  # Sort to maintain order
        
        for index, filename in enumerate(files, start=start_number):
            old_path = os.path.join(folder_path, filename)
            
            if os.path.isfile(old_path):  # Ensure it's a file
                extension = os.path.splitext(filename)[1]  # Keep original extension
                new_filename = f"{prefix}{index}{extension}"
                new_path = os.path.join(folder_path, new_filename)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
    
        print("All files renamed successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
folder = r"path/to/your/folder"  # Replace with your folder path
rename_files(folder)
