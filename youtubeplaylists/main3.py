from pytube import Playlist
import os
from multiprocessing.pool import ThreadPool

# Function to sanitize filename
def sanitize_filename(filename):
    invalid_chars = '/\\?%*:|"<>!'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

# Function to download a single video
def download_video(video):
    try:
        index, video = video
        video_title = f"{index}. {sanitize_filename(video.title)}"
        print(f"Downloading video: {video_title}")

        # Get the stream with the highest resolution
        stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Download the selected stream
        stream.download(output_path=output_path, filename=f"{video_title}.mp4")
        print(f"Download completed: {video_title}")
    except Exception as e:
        print(f"Error downloading {video_title}: {e}")

# Take input URL of the playlist from the user
playlist_url = input("Enter the URL of the playlist: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Get the channel name from the first video
first_video = playlist.videos[0]
channel_name = sanitize_filename(first_video.author)

# Create the directory path for saving the playlist videos
output_path = os.path.join("E:/studymaterial", channel_name)

# Create a thread pool for parallel downloading
pool = ThreadPool()

# Download each video in the playlist concurrently
results = pool.map(download_video, enumerate(playlist.videos, start=1))

# Close the pool
pool.close()
pool.join()
