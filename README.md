# youtubeChannelOpenerScript
 This Python script opens a list of YouTube channels in your default browser one by one with a short delay. It's useful if you want to visit multiple channels quickly.

Step-by-Step Tutorial to Run the YouTube Channel Opener Script

Step 1: Install Python

	1.	Go to the Python website.
	2.	Download the latest version for your operating system.
	3.	During installation, check the box that says “Add Python to PATH” to make sure you can run Python from any terminal.

Step 2: Set Up the Script File

	1.	Open a text editor (e.g., Notepad, VS Code).
	2.	Copy and paste the following code into the editor:

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
