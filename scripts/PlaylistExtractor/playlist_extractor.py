import os
import pytube
import ffmpeg
import shutil
import csv
from tqdm import tqdm

# Ensure download folder exists
download_folder = "/content/YT_Downloads"
os.makedirs(download_folder, exist_ok=True)

# Video Metadata export function
def export_metadata(video_list):
    """Exports video metadata (title, description, URL) to a CSV file."""
    with open("video_metadata.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "URL"])
        for video in video_list:
            writer.writerow([video.title, video.description, video.watch_url])
    print("Metadata exported to video_metadata.csv")

# Progress Bar Callback
def progress_function(stream, chunk, bytes_remaining):
    """Updates the progress bar during the download."""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size * 100
    tqdm.write(f"Downloading... {progress:.2f}%")

# Video Download Function with Progress Bar
def download_video(video_url, naming_convention="title"):
    """Downloads a YouTube video with a custom naming convention and progress bar."""
    video = pytube.YouTube(video_url, on_progress_callback=progress_function)
    stream = video.streams.get_highest_resolution()  # Change as needed
    video_title = video.title if naming_convention == "title" else f"video_{video.streams.index(stream)}"
    output_file = os.path.join(download_folder, f"{video_title}.mp4")
    stream.download(output_file=output_file)
    print(f"Downloaded: {output_file}")
    return video  # Return video object for metadata export

# Batch Conversion Function
def batch_convert_to_format(input_folder, output_format="mp3"):
    """Batch converts all MP4 videos in a folder to a different format (MP3, etc.)."""
    files = os.listdir(input_folder)
    for file in files:
        if file.endswith(".mp4"):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.splitext(input_file)[0] + f".{output_format}"
            ffmpeg.input(input_file).output(output_file).run()
            print(f"Converted {input_file} to {output_file}")

# Download Playlist and Process Each Video
def download_playlist(playlist_url, format_choice, naming_convention):
    """Downloads an entire YouTube playlist with custom format and naming convention."""
    playlist = pytube.Playlist(playlist_url)
    print(f"\nDownloading Playlist: {playlist.title}")
    
    video_list = []
    for video_url in tqdm(playlist.video_urls, desc="Downloading", unit="video"):
        try:
            video = download_video(video_url, naming_convention=naming_convention)
            video_list.append(video)  # Collect videos for metadata export
        except Exception as e:
            print(f"Error downloading {video_url}: {e}")

    # Export metadata after download is complete
    export_metadata(video_list)

    print("\nPlaylist Download Complete!")

# User Input Section
playlist_url = input("Enter YouTube Playlist URL: ").strip()
format_choice = input("Choose format - MP4 (video) or MP3 (audio): ").strip().lower()
naming_convention = input("Choose naming convention - 'title' or 'index': ").strip().lower()

if format_choice not in ["mp3", "mp4"]:
    print("Invalid choice! Please enter 'mp3' or 'mp4'.")
else:
    download_playlist(playlist_url, format_choice, naming_convention)

    # Batch convert videos in the folder after download
    convert_format = input("Do you want to batch convert the videos to a different format (e.g., mp3)? (y/n): ").strip().lower()
    if convert_format == 'y':
        output_format = input("Enter the desired output format (e.g., mp3, mkv, etc.): ").strip().lower()
        batch_convert_to_format(download_folder, output_format)
