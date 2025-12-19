## `ClipboardGuardian.py`
This Python script runs in the background and automatically organizes copied text and manages your clipboard history. This script allows you to:

✔️Automatically save clipboard content with customizable categories.

✔️Export/import clipboard history for backup or transfer.

✔️Use a GUI to view, copy, delete, and search through clipboard history.

✔️Sync clipboard history to Google Drive.

✔️Automatically detect and filter out  sensitive data, such as passwords or API keys.

## Install Dependencies
Before running the script, make sure you have the following dependencies installed:
- `pyperclip`: To interact with the clipboard.
- `keyboard`: To capture keyboard hotkeys.
- `tkinter`: For creating the GUI interface.
- `pandas`: For handling export functionality.
- `gspread`: To interact with Google Sheets for cloud syncing.
- `oauth2client`: For Google Sheets authentication.

You can install the required libraries using `pip`:
```bash
pip install pyperclip keyboard pandas gspread oauth2client tkinter
```

## Configuration
### 🔹️Google Drive Sync Setup
To enable Google Drive sync, follow these steps:
1. **Create Google API credentials**:
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Enable the **Google Sheets API**.
    - Create a **Service Account** and download the **JSON key file** (e.g., `credentials.json`).
    - Save the `credentials.json` file in the same directory as the script.
2. **Share Google Sheet**:
    - Create a Google Sheet in your Google Drive.
    - Share it with the service account email found in the `credentials.json`.

### 🔹️Custom Categories
The script uses a `config.json` file for defining custom categories and keywords for clipboard classification.

The default `config.json` looks like this:
```json
{
    "URL": ["http", "https", "www"],
    "Email": ["@gmail.com", "@yahoo.com"],
    "Code": ["def ", "class ", "function ", "return "],
    "Sensitive": ["password", "api_key", "secret", "token"]
}
```
You can edit this file to add or modify categories and associated keywords.

## How to Use
### 1️⃣ Run the Script   
Execute the script by running:
```bash
python ClipboardGuardian.py
```
The script will run in the background, monitoring your clipboard for any new text that you copy.
    
### 2️⃣ Clipboard Monitoring
The script automatically saves copied text to the clipboard database. It classifies content into categories like `URL`, `Email`, `Code`, or `Text`.
    
### 3️⃣ View Clipboard History (GUI)
Press **Ctrl + Shift + S** to open the GUI and view your clipboard history. The GUI displays clipboard entries categorized and sorted by the most recent first.You can *copy*, *delete*, or *export* clipboard entries from the list.

### 4️⃣ Export Clipboard History
- In the GUI, click the **Export** button to save your clipboard history to a `.csv` or `.txt` file.
- You will be prompted to choose a location to save the file.

### 5️⃣ Import Clipboard History
- You can import previously saved clipboard history by clicking the **Import** button.
- Select the `.csv` or `.txt` file containing your clipboard history to restore it into the database.

### 6️⃣ Sync to Google Drive
Click the **Sync to Drive** button in the GUI to sync your clipboard history to a Google Sheet. The history will be stored in the specified Google Sheet and updated automatically.

### 7️⃣ Sensitive Data Filtering
If clipboard content is detected as sensitive (e.g., containing "password", "api_key"), it will not be saved. The script will print a message indicating that sensitive data was ignored.

## Keyboard Shortcuts
- **Ctrl + Shift + S**: Open the clipboard history GUI to view, search, copy, or delete entries.
- **Ctrl + C** (in GUI): Copy selected clipboard entry to clipboard.
- **Ctrl + D** (in GUI): Delete selected clipboard entry from the database.
- **Ctrl + E** (in GUI): Export clipboard history to a `.csv` or `.txt` file.
- **Ctrl + I** (in GUI): Import clipboard history from a `.csv` or `.txt` file.
- **Ctrl + G** (in GUI): Sync clipboard history to Google Drive.

## Troubleshooting
### 🔺️ Google Drive Sync Issues
- Ensure that the **Google Sheets API** is enabled in the [Google Cloud Console](https://console.cloud.google.com/).
- Check if the `credentials.json` file is correctly set up and accessible by the script.
- Make sure the Google Sheet is shared with the service account email (found in the `credentials.json`).

### 🔺️ Clipboard History Not Being Saved
- Check the `config.json` file to make sure that categories and keywords are properly defined.
- Verify that the clipboard content doesn't contain sensitive data (e.g., passwords) that would cause it to be excluded.
