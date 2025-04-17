#!/usr/bin/env python3
import yt_dlp

def download_video(url: str, output_path: str) -> None:
    """Download a video from a URL and save it to the specified output path."""
    ydl_opts = {

        'format': 'bestvideo+bestaudio/best',
#        'format': 'best',  # Choose the best quality available
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output file format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    video_url = input("Enter the video URL: ")  # Prompt user for video URL
    output_directory = input("Enter the output directory: ")  # Prompt user for output directory
    download_video(video_url, output_directory)
    print("Download complete!")

