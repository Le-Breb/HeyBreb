import os
import shlex

def search_handler(query):
    url = f"https://www.google.com/search?q={query}"
    safe_url = shlex.quote(url)  # Safely quote the URL
    print(f"Opening URL: {url}")
    os.system(f"google-chrome {safe_url} &")

def stop_handler(query):
    print("Stopping the assistant.")
    os._exit(0)
