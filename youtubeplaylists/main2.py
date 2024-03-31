from pytube import YouTube

# Take input URL of the video from the user
video_url = input("Enter the URL of the video: ")

try:
    # Create a YouTube object for the video
    yt = YouTube(video_url)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Download the video
    print("Downloading video...")
    stream.download(output_path="E:/studymaterial/")  # Change the output_path as needed
    print("Download completed!")

except Exception as e:
    print(f"Error downloading the video: {e}")
