import requests
import os


def download_reel(video_url, filename="reel.mp4"):
    response = requests.get(video_url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename


def repost_reel(cl, reel, caption="🗿🗿🫠"):
    video_url = reel.video_url
    video_path = download_reel(video_url)

    # Ensure the file exists before attempting to post
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Failed to download video from {video_url}")

    cl.clip_upload(video_path, caption)
    os.remove(video_path)  # Clean up the downloaded file
