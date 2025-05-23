from pathlib import Path

from pytubefix import YouTube
from pytubefix.cli import on_progress


class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path.cwd()
        self.yt = YouTube(self.url,
                          on_progress_callback=on_progress,
                          on_complete_callback=self.on_complete)
        self.resolutions = [stream.resolution for stream in self.yt.streams.filter(progressive=True)]

        # Set quality to the highest available if not specified
        self.quality = quality if quality in self.resolutions else self.yt.streams.get_highest_resolution(progressive=True).resolution

    def download(self):
        self.yt.streams.get_by_resolution(self.quality).download(output_path=self.output_path)

    # List available resolutions
    def list_resolutions(self):
        return self.resolutions

    # What to do when download is complete
    def on_complete(self, stream, file_path):
        print(f"Download completed: {file_path}")
        print(f"File size: {Path(file_path).stat().st_size / (1024 * 1024):.2f} MB")
        print(f"Video title: {self.yt.title}")
        print(f"Video resolution: {stream.resolution}")
        print(f"Video URL: {self.url}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output path (leave blank for current directory): ")
    YouTubeDownloader(url=url, output_path=output_path).download()