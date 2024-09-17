import os
import time
from instaloader import Instaloader, Profile
from instagrapi import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Instagram credentials from .env file
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
TARGET_USER_ID = os.getenv('TARGET_USER_ID')
UPLOAD_DIRECTORY = "down"
RETRY_LIMIT = 3
RETRY_DELAY = 10  # seconds between retries

# Initialize Instaloader and Instagrapi clients
instaloader = Instaloader()
instagrapi_client = Client()

def login_instagram():
    instagrapi_client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

def download_videos(username):
    profile = Profile.from_username(instaloader.context, username)
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
    for post in profile.get_posts():
        if post.is_video:
            video_path = os.path.join(UPLOAD_DIRECTORY, f"{post.date_utc.isoformat()}.mp4")
            if not os.path.exists(video_path):
                instaloader.download_post(post, target=UPLOAD_DIRECTORY)

def upload_video(video_path):
    retries = 0
    while retries < RETRY_LIMIT:
        try:
            print(f"Uploading: {video_path}")
            media = instagrapi_client.video_upload(video_path, caption="Uploaded via script")
            print(f"Video uploaded successfully: {media.pk}")
            os.remove(video_path)  # Remove the file after successful upload
            return True
        except Exception as e:
            print(f"Upload failed: {e}")
            retries += 1
            print(f"Retrying ({retries}/{RETRY_LIMIT}) in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
    return False

def process_videos():
    login_instagram()
    download_videos(TARGET_USER_ID)
    for filename in os.listdir(UPLOAD_DIRECTORY):
        if filename.endswith(".mp4"):
            video_path = os.path.join(UPLOAD_DIRECTORY, filename)
            success = upload_video(video_path)
            if not success:
                print(f"Failed to upload {video_path} after {RETRY_LIMIT} attempts.")
                # Optionally handle the failed upload (e.g., log or notify)

if __name__ == "__main__":
    process_videos()
