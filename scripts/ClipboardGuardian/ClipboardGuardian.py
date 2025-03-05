import time
import sqlite3
import pyperclip
import keyboard
import json
import re
import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Database Setup
conn = sqlite3.connect("clipboard_history.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clipboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        content TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# Load Custom Categories
def load_categories():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        default_categories = {
            "URL": ["http", "https", "www"],
            "Email": ["@gmail.com", "@yahoo.com"],
            "Code": ["def ", "class ", "function ", "return "],
            "Sensitive": ["password", "api_key", "secret", "token"]
        }
        with open("config.json", "w") as file:
            json.dump(default_categories, file, indent=4)
        return default_categories

categories = load_categories()

# Categorize Text
def categorize_text(text):
    for category, keywords in categories.items():
        if any(keyword in text.lower() for keyword in keywords):
            return category
    return "Text"

# Ignore Sensitive Data
def is_sensitive(text):
    return categorize_text(text) == "Sensitive"

# Save Clipboard Data
def save_clipboard(content):
    if is_sensitive(content):
        print("Sensitive data detected, not saving.")
        return
    category = categorize_text(content)
    cursor.execute("INSERT INTO clipboard (category, content) VALUES (?, ?)", (category, content))
    conn.commit()
    print(f"Saved {category}: {content[:50]}...")

# Monitor Clipboard
def monitor_clipboard():
    last_clipboard = ""
    print("Clipboard Organizer running... Press 'Ctrl + Shift + S' to search.")
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content and clipboard_content != last_clipboard:
            save_clipboard(clipboard_content)
            last_clipboard = clipboard_content
        time.sleep(1)

# Export Clipboard History
def export_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt")])
    if file_path:
        df = pd.read_sql_query("SELECT * FROM clipboard", conn)
        if file_path.endswith(".csv"):
            df.to_csv(file_path, index=False)
        else:
            df.to_csv(file_path, index=False, sep="\t")
        messagebox.showinfo("Export", "Clipboard history exported successfully.")

# Import Clipboard History
def import_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt")])
    if file_path:
        df = pd.read_csv(file_path)
        df.to_sql("clipboard", conn, if_exists="append", index=False)
        messagebox.showinfo("Import", "Clipboard history imported successfully.")

# Google Drive Sync
def sync_to_drive():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("Clipboard_History").sheet1
        df = pd.read_sql_query("SELECT * FROM clipboard", conn)
        sheet.clear()
        sheet.insert_rows([df.columns.tolist()] + df.values.tolist())
        messagebox.showinfo("Cloud Sync", "Clipboard history synced to Google Drive.")
    except Exception as e:
        messagebox.showerror("Cloud Sync Error", str(e))

# GUI for Clipboard History
def open_gui():
    root = tk.Tk()
    root.title("Clipboard History")
    root.geometry("600x400")

    def load_data():
        cursor.execute("SELECT id, category, content FROM clipboard ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        listbox.delete(0, tk.END)
        for row in rows:
            listbox.insert(tk.END, f"[{row[1]}] {row[2][:100]}...")

    def delete_selected():
        selected = listbox.curselection()
        if not selected:
            return
        item = listbox.get(selected[0])
        entry_id = item.split("]")[0][1:]
        cursor.execute("DELETE FROM clipboard WHERE id=?", (entry_id,))
        conn.commit()
        load_data()

    def copy_selected():
        selected = listbox.curselection()
        if not selected:
            return
        item = listbox.get(selected[0])
        content = item.split("] ")[1]
        pyperclip.copy(content)
        messagebox.showinfo("Copied", "Text copied to clipboard.")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, width=80, height=15, yscrollcommand=scrollbar.set)
    listbox.pack()
    scrollbar.config(command=listbox.yview)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Copy", command=copy_selected).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Delete", command=delete_selected).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Export", command=export_data).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Import", command=import_data).grid(row=0, column=3, padx=5)
    tk.Button(button_frame, text="Sync to Drive", command=sync_to_drive).grid(row=0, column=4, padx=5)

    load_data()
    root.mainloop()

# Hotkeys
keyboard.add_hotkey("ctrl+shift+s", open_gui)

# Run Clipboard Monitor
if __name__ == "__main__":
    try:
        monitor_clipboard()
    except KeyboardInterrupt:
        print("\nClipboard Organizer stopped.")
        conn.close()
