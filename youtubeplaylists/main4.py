from pytube import Playlist
import os
import concurrent.futures

# Function to sanitize filename
def sanitize_filename(filename):
    invalid_chars = '/\\?%*:|"<>!'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

# Function to download a single video
def download_video(video):
    index, video = video
    video_title = f"{index}. {sanitize_filename(video.title)}"
    try:
        print(f"Downloading video: {video_title}")
        stream = video.streams.get_highest_resolution()
        if stream:
            stream.download(output_path=output_path, filename=f"{video_title}.mp4")
            print(f"Download completed: {video_title}")
            return True
        else:
            print(f"No stream available for {video_title}")
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

# Create the directory path for saving the playlist videos
output_path = os.path.join("E:/studymaterial", channel_name)

# Create a ThreadPoolExecutor for parallel downloading
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Download each video in the playlist concurrently
    results = executor.map(download_video, enumerate(playlist.videos, start=1))

# Process the results
successful_downloads = sum(results)
total_videos = len(playlist.videos)
print(f"Total videos downloaded: {successful_downloads}/{total_videos}")
