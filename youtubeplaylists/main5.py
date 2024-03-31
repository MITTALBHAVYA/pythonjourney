from pytube import Playlist
import os
import concurrent.futures

# Function to sanitize filename
def sanitize_filename(filename):
    invalid_chars = '/\\?%*:|"<>!'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

# Function to download only mp3 version or music of a single video
def download_mp3(video):
    index, video = video
    video_title = f"{index}. {sanitize_filename(video.title)}"
    try:
        print(f"Downloading mp3 of video: {video_title}")
        stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
        if stream:
            stream.download(output_path=output_path, filename=f"{video_title}.mp3")
            print(f"Download completed: {video_title}")
            return True
        else:
            print(f"No mp3 stream available for {video_title}")
            return False
    except Exception as e:
        print(f"Error downloading {video_title}: {e}")
        return False

# Take input URL of the playlist from the user
playlist_url = input("Enter the URL of the playlist: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Get the channel name from the first video
first_video = playlist.videos[0]
channel_name = sanitize_filename(first_video.author)

# Define the output path to the USB drive
output_path = os.path.join("H:", channel_name)

# Create the directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Create a ThreadPoolExecutor for parallel downloading
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Download mp3 version of each video in the playlist concurrently
    results = executor.map(download_mp3, enumerate(playlist.videos, start=1))

# Process the results
successful_downloads = sum(results)
total_videos = len(playlist.videos)
print(f"Total mp3 downloaded: {successful_downloads}/{total_videos}")
