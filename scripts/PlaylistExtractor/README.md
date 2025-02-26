## `playlist_extractor.py`

This Python script allows you to:
- Extract & download entire YouTube playlists.
- Convert videos into MP4 (video) or MP3 (audio).
- Customize video file names.
- Export video metadata (title, description, URL) to a CSV file.
- Optionally, batch convert videos to a different format.

## Install Dependencies
Copy and paste the following code in the cell to install all required libraries:

```python
!pip install pytube ffmpeg-python tqdm
!apt-get install ffmpeg -y
```

This will install:
- **`pytube`**: For downloading YouTube videos.
- **`ffmpeg`**: For converting videos to different formats.
- **`tqdm`**: For displaying a progress bar during downloads.

## Setup Google Drive _(Optional Google Colab)_
If you want to save downloaded videos and files directly to Google Drive, you need to **mount your Google Drive**. To do this, run the following code:

```python
from google.colab import drive
drive.mount('/content/drive')

# Set the folder where files will be stored
download_folder = "/content/drive/My Drive/YT_Playlist_Downloads"
```

A prompt will appear asking you to authorize Google Drive. Follow the instructions to grant access.

_If you don't want to use Google Drive, you can skip this step and store files in the local directory (`/content/YT_Downloads`)._

## Run the script 
> **Run the script `playlist_extractor.py` or Copy and paste into the next cell of your Google Colab notebook to execute the script.**

## User Input Prompts
The script will prompt you for the following inputs:
1. **YouTube Playlist URL**: Paste the YouTube playlist link (e.g., `https://www.youtube.com/playlist?list=...`).
2. **Format Choice**: Choose either `mp4` (video) or `mp3` (audio).
3. **Naming Convention**: Choose between `title` (use video title as filename) or `index` (use video position in playlist).

Example input/output in the notebook:
```python
Enter YouTube Playlist URL: https://www.youtube.com/playlist?list=...
Choose format - MP4 (video) or MP3 (audio): mp4
Choose naming convention - 'title' or 'index': title
```

## Batch Conversion (Optional)
After downloading the videos, you will be asked if you want to **batch convert** them to a different format (e.g., MP3).

Example input/output:
```
Do you want to batch convert the videos to a different format (e.g., mp3)? (y/n): y
Enter the desired output format (e.g., mp3, mkv, etc.): mp3
```

## Verify Output
1. **Downloaded Files**:
    - Go to your **Google Drive** folder (`YT_Playlist_Downloads`) or the local folder `/content/YT_Downloads`.
    - Check if the videos are downloaded in the chosen format (MP4 or MP3).
2. **Metadata**:
    - A **`video_metadata.csv`** file will be created in the same directory. Open this file to check the metadata of each video (title, description, and URL).
3. **Batch Conversion**:
    - If you chose to batch convert the videos, check the folder to confirm that the files are now in the new format (e.g., MP3).

## Troubleshooting
- **Video Not Downloading**: If a video fails to download, it might be due to an issue with `pytube`. Retry the script, or try using a different video URL.
- **Incorrect Format Conversion**: Ensure that `ffmpeg` is installed correctly. If conversion fails, check if the input format is correct.

### ▉ Happy Extracting!
