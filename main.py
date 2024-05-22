import os
from dotenv import load_dotenv
from login import login_instagram
from fetch_reels import fetch_reels
from repost_reels import repost_reel

load_dotenv()

def main():
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    target_username = 'Krisslinux99'  # Change this to the desired username

    # Define the proxy information
    proxy = {
        'http': '197.210.8.46:52026',
    }

    # Log in to Instagram with proxy
    cl = login_instagram(username, password, proxy=proxy)
    
    # Fetch Reels from the target user
    reels = fetch_reels(cl, target_username)
    
    # Repost the first reel as an example
    if reels:
        reel = reels[0]
        repost_reel(cl, reel, caption=f'🗿🗿')

if __name__ == "__main__":
    main()