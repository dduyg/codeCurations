# `file_tidy.py`

The `file_tidy.py` script is designed to help organize files in a given directory by categorizing them based on their extensions. It moves files into separate subfolders corresponding to different categories such as `Images`, `Documents`, `Audio`, `Videos`, `Archives`, `Code`, and `Others`. Files that don't match any of the predefined categories are moved to the "Others" folder.

The script also logs the actions performed (file movements) to a log file, `file_organizer.log`, to maintain a record of the organization process.

## How to Use

### 1️⃣ Prepare the Directory

Ensure that the directory you want to organize is ready. The script will reorganize all files in the given directory and its subdirectories.

### 2️⃣ Run the Script

1. Save the script as `file_tidy.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `file_tidy.py` is saved.
4. Run the script by typing:

```bash
python file_tidy.py
```

### 3️⃣ Provide the Directory Path

When prompted, enter the path of the directory you want to organize. For example:

```
Enter the path of the directory you want to organize: /path/to/your/folder
```

### 4️⃣ Check the Organization and Log

- The script will create subfolders for each category in the specified directory.
- It will move the files to the appropriate subfolder based on their extensions.
- After the process is complete, the terminal will display "File organization complete!" and a log file (`file_organizer.log`) will be created in the same directory where the script is run. The log file contains detailed information about the file movements.

## Logging

The script generates a log file named `file_organizer.log` to record the actions taken. The log includes:

- File movements (from source to destination).
- Timestamps for each action.
- Errors (if any directory does not exist).

## <samp>Example Log Output</samp>

```
2025-02-27 12:34:56,789 - INFO - Created folder: /path/to/your/folder/Images
2025-02-27 12:35:01,123 - INFO - Moved photo.jpg from /path/to/your/folder to Images folder.
2025-02-27 12:35:10,456 - INFO - Moved document.pdf from /path/to/your/folder to Documents folder.
2025-02-27 12:35:15,789 - INFO - Moved video.mp4 from /path/to/your/folder to Videos folder.
2025-02-27 12:35:20,234 - INFO - File organization complete!
```

## Troubleshooting

**🔹️ Directory Not Found**: If the provided directory path does not exist, the script will log an error and display an error message.

**🔹️ Permissions**: Ensure the script has sufficient permissions to read from the source directory and write to the destination folders.