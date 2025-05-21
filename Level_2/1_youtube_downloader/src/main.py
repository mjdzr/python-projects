import argparse
from pathlib import Path
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=5qF_qbaWt3Q"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution(progressive=True)
ys.download()