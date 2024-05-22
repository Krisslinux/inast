# Modify the login_instagram function in login.py

from instagrapi import Client

def login_instagram(username, password, proxy=None):
    proxy_url = f"{list(proxy.keys())[0]}://{list(proxy.values())[0]}" if proxy else None
    cl = Client(proxy=proxy_url)  # Pass the proxy information while creating Client instance
    cl.login(username, password)
    return cl