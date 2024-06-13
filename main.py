import os
import shutil
import pathlib
import time

# Paths to move files to
directories = {
    'pdf': os.path.expanduser("~/Documents/PDFs"),
    'jpg': os.path.expanduser("~/Pictures"),
    'png': os.path.expanduser("~/Pictures"),
    'jpeg': os.path.expanduser("~/Pictures"),
    'gif': os.path.expanduser("~/Pictures"),
    'mp4': os.path.expanduser("~/Videos"),
    'mp3': os.path.expanduser("~/Music"),
    'wav': os.path.expanduser("~/Music"),
    'docx': os.path.expanduser("~/Documents"),
    'xlsx': os.path.expanduser("~/Documents"),
    'pptx': os.path.expanduser("~/Documents"),
    'txt': os.path.expanduser("~/Documents"),
    # File types that are going into the D Drive
    'zip': 'D:/Downloads/All Downloads/Archived',
    'rar': 'D:/Downloads/All Downloads/Archived',
    '7z': 'D:/Downloads/All Downloads/Archived',
    'iso': 'D:/Downloads/All Downloads/Archived',
    'exe': 'D:/Downloads/All Downloads/Executables',
    'msi': 'D:/Downloads/All Downloads/Executables',
    'fbx': 'D:/Downloads/All Downloads/3D',
    'blend': 'D:/Downloads/All Downloads/3D',
    'torrent': 'D:/Downloads/All Downloads/Torrented Files',
    'CT': 'D:/Downloads/All Downloads/Cheat Engine Tables',
    'ttf': 'D:/Downloads/All Downloads/Fonts',
    'otf': 'D:/Downloads/All Downloads/Fonts',
    'psd': 'D:/Downloads/All Downloads/Photoshop Files',
    'ai': 'D:/Downloads/All Downloads/Illustrator Files',
    'svg': 'D:/Downloads/All Downloads/SVG Files',
    'ini': 'D:/Downloads/All Downloads/Configuration Files',
    'cs': 'D:/Downloads/All Downloads/Program Scripts/C#',
    'jar': 'D:/Downloads/All Downloads/Program Scripts/Java',
    'bat': 'D:/Downloads/All Downloads/Program Scripts/Batch',
    'unitypackage': 'D:/Downloads/All Downloads/Unity Packages',
    #Everything else goes into the Miscellaneous folder
    '': 'D:/Downloads/All Downloads/Miscellaneous'

}



# Path to default Downloads folder
default_downloads = 'D:/Downloads/All Downloads'

# Function to organise files automatically
def organise_files(source_dir):
    print("Organising files...")
    for file in os.listdir(source_dir):  # Iterate through all files in the source directory
        OriginalFilePath = os.path.join(source_dir, file) # The unchanged path of the file
        item_path = os.path.join(source_dir, file)  # Get the full path of the file

        if os.path.isfile(item_path):  # Check if the item is a file
            file_extension = pathlib.Path(item_path).suffix.lower().strip('.')  # Get the file extension of the file
            destination_dir = directories.get(file_extension, None)  # Get the destination directory for the file extension

            if destination_dir:  # Check if the destination directory exists
                os.makedirs(destination_dir, exist_ok=True)  # Create the destination directory if it doesn't exist
                try:
                    shutil.move(item_path, destination_dir)  # Move the file to the destination directory
                    print(f"Moved {file} from {OriginalFilePath} to {destination_dir}")
                except shutil.Error as e:
                    print(f"Error moving {file}: {e}")  # Print error message if file can't be moved
    print("Organising files complete!")


    #We need to track the changes made
# Main function
def main():
    while True:
        organise_files(default_downloads)  # Organise files in the default Downloads folder
        time.sleep(120)  # Wait for 2 minutes before organising files again

if __name__ == '__main__':
    main()
