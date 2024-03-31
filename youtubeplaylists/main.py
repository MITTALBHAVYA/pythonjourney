from pytube import Playlist
import os

# Function to sanitize filename
def sanitize_filename(filename):
    invalid_chars = '/\\?%*:|"<>!'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

# Take input URL of the playlist from the user
playlist_url = input("Enter the URL of the playlist: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Get the channel name from the first video
first_video = playlist.videos[0]
channel_name = sanitize_filename(first_video.author)

# Create the directory path for saving the playlist videos
output_path = os.path.join("E:/studymaterial", channel_name)

# Loop through each video in the playlist and download it
for index, video in enumerate(playlist.videos, start=1):
    try:
        video_title = f"{index}. {sanitize_filename(video.title)}"
        print(f"Downloading video: {video_title}")
        video.streams.get_highest_resolution().download(output_path=output_path, filename=f"{video_title}.mp4")
        print(f"Download completed: {video_title}")
    except Exception as e:
        print(f"Error downloading {video_title}: {e}")
