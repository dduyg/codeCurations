## `quick_rename.py`
Here’s a Python script to batch rename multiple files in a folder according to a specific pattern, like adding a prefix or suffix to filenames, or date-based renaming.

> ### How it works:
> - **`directory`**: The folder path where the files are located.
> - **`prefix`**: The string to add at the beginning of each filename (optional).
> - **`suffix`**: The string to add at the end of each filename (optional).
> - **`add_date`**: If set to `True`, it adds the current date (`YYYY-MM-DD`) at the beginning of each filename.

## Example:
Let’s say you have files like:
```
document1.txt
document2.txt
image.png
```
And you set the prefix to `'new_'`, suffix to `'_backup'`, and enable the date option, the files will be renamed like:
```
2025-02-25_new_document1_backup.txt
2025-02-25_new_document2_backup.txt
2025-02-25_new_image_backup.png
```

## How to run:
- Save the script as `quick_rename.py`
- Replace `path_to_your_folder` with the directory path where your files are stored
- Run the script from the command line by typing:
  ```
  python quick_rename.py
  ```
This will rename all the files in the specified directory based on your parameters!
