
# YouTube Video Downloader

## Description

This Python script enables you to download your own YouTube videos directly to your local machine. It utilizes the `yt-dlp` library, a powerful tool for downloading videos from YouTube and other platforms.

**Important:** This script should **only** be used to download videos that you own or have explicit permission to download.

## Prerequisites

- Python 3 installed
- Virtual Environment (`venv`) module installed

## Setup Instructions

### 1. Clone or Copy the Script

Ensure you have the script file saved locally (e.g., `download_video.py`).

### 2. Set Up Virtual Environment

Create and activate a virtual environment to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the libraries:

```bash
pip install -r requirements.txt
```

## How to Use

Run the script by executing:

```bash
python download_video.py
```

Follow the interactive prompts:

- **Enter the video URL:** Paste the URL of your own YouTube video.
- **Enter the output directory:** Provide the directory path where you wish to save the downloaded video.

Example:

```
Enter the video URL: https://www.youtube.com/watch?v=example
Enter the output directory: /home/user/videos
```

Upon completion, you will see:

```
Download complete!
```

## Usage Policy

- **Only download videos that you own or have explicit rights to download.**
- **Do NOT** use this tool for downloading copyrighted content without explicit permission from the content owner.

## License

Specify your project's license here (e.g., MIT License).