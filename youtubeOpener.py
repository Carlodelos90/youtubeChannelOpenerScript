import webbrowser
import time

# List of YouTube channel URLs
urls = [
    'https://www.youtube.com/channel/CHANNEL_ID1',
    'https://www.youtube.com/channel/CHANNEL_ID2',
    # Add more URLs here
]

# Open each URL in the default web browser
for url in urls:
    webbrowser.open(url)
    time.sleep(1)  # Adjust the sleep time if necessary