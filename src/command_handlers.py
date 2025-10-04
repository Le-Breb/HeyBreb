import os

def search_handler(query):
    print(query)
    url = f"https://www.google.com/search?q={query}"
    print(f"Opening URL: {url}")
    os.system(f"google-chrome '{url}' &")

def stop_handler(query):
    print("Stopping the assistant.")
    os._exit(0)
