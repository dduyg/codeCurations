## `file_tidy.py`
This Python script automatically organizes files in a specified directory into folders based on their file types (e.g., images, documents, videos, archives, scripts, etc.) to save time and help keep your workspace tidy. It creates subfolders for each file type category and moves the corresponding files into them.

## How to use the script
### 1️⃣ Download/Clone the repository
You can either clone the repository (if hosted) or simply download the `file_tidy.py` file.

### 2️⃣ Modify the `TARGET_DIR` variable
Open the script file (`file_tidy.py`) and change the `TARGET_DIR` variable to the path of the directory you want to organize.    

```python
TARGET_DIR = "/path/to/your/directory"  # Change this to your target directory
```
    
### 3️⃣ Run the script
Open your terminal/command prompt. Navigate to the directory where `file_tidy.py` is saved. Run the script using the following command:

```bash
python file_tidy.py
```
    
### 4️⃣ Organizing Process
The script will:
- Create subdirectories for different file categories (Images, Documents, Videos, Audio, Archives, Scripts, and Other).
- Move the files into their corresponding categories based on file extensions.
- Files that don’t match any defined category will be moved into the "Other" folder.

## Customization
- **File Categories**: The script is already set up to recognize common file types for categories like images, documents, videos, audio, etc. You can modify the `FILE_CATEGORIES` dictionary to add more categories or file types.
    
    ```python
    FILE_CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
        "Scripts": [".py", ".sh", ".bat", ".js", ".css", ".html"],
        "Other": []  # Files that don't match any category will go here
    }
    ```
    
- **Directory Structure**: The script creates subdirectories based on the categories defined. Feel free to change the structure by modifying the script.

## <samp>Example Directory Structure After Running the Script</samp>
```
/path/to/your/directory/
├── Images/
│   ├── photo1.jpg
│   ├── image2.png
├── Documents/
│   ├── resume.pdf
│   ├── report.docx
├── Videos/
│   ├── movie.mp4
│   ├── clip.mkv
├── Audio/
│   ├── song.mp3
│   ├── podcast.wav
├── Archives/
│   ├── archive.zip
│   ├── backup.tar
├── Scripts/
│   ├── file_organizer.py
│   ├── automation.sh
└── Other/
    ├── randomfile.xyz
```

## Troubleshooting
- **Error: `The directory does not exist`**: Make sure the `TARGET_DIR` is correctly set to the path of an existing directory.

- **The script doesn't move files**:
    - Double-check that the files have extensions that match those defined in the `FILE_CATEGORIES` dictionary.
    - Ensure the script has permission to read from the source directory and write to the destination directories.
