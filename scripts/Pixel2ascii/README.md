## `pixel2ascii.py`
This Python script converts images into ASCII art and either displays the result in the terminal or saves it as a text file. It supports batch processing for multiple images and can process an entire folder or specific images.

### Features
✔ Convert **single or multiple** images into ASCII art

✔ Supports batch processing for an entire folder or only selecting specific images

✔ Saves each ASCII output in a separate `.txt` file.

✔ Supports **JPG, PNG, GIF, BMP, and JPEG** formats

## Install Dependencies
Before running the script, install the required dependency:
```
pip install pillow
```

## How to Use
You can use the script in **three ways**:

### 1. Convert an Entire Folder of Images
Converts all images inside a specified folder and saves the ASCII text files in `ascii_output/` folder:
```
python ascii_art.py -f /path/to/image_folder
```

Optionally, specify a custom output directory:
```
python ascii_art.py -f /path/to/image_folder -o /path/to/output_folder
```

### 2. Convert Specific Images
If you want to convert only certain images, provide their filenames:
```
python ascii_art.py -i 04.jpg 06.png 07.png
```

Save the output to a specific folder:
```
python ascii_art.py -i 04.jpg 06.png 07.png -o ascii_results
```

### 3. Adjust ASCII Output Width
For higher resolution, adjust the ASCII width:
```
python ascii_art.py -f /path/to/image_folder -w 150
```

This increases the image width to *150 characters*, making the ASCII art more detailed.

## Troubleshooting
🔹 **Error: Unable to open image.**

- Check if the file path is correct.
- Ensure the file format is supported.

🔹 **ASCII output looks too small or distorted.**

- Try increasing the width using `w 150` for better resolution.

🔹 **Permission denied when saving output.**

- Try running the script with **admin privileges** or use a different output directory.
