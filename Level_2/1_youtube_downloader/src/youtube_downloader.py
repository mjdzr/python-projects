import argparse
from pathlib import Path

from pytubefix import YouTube
from pytubefix.cli import on_progress


class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path if output_path else Path.cwd()
        self.yt = YouTube(self.url,
                          on_progress_callback=on_progress,
                          on_complete_callback=self.on_complete)
        self.resolutions = [stream.resolution for stream in self.yt.streams.filter(progressive=True)]

        # Set quality to the highest available if not specified
        if quality not in self.resolutions and quality is not None:
            print(f"Quality '{quality}' not found. Available resolutions: {self.resolutions}. Highest resolution will be used instead.")
            quality = None
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
    parser = argparse.ArgumentParser(
        description="Download YouTube videos."
        )

    parser.add_argument("-u", "--url", type=str, required=True, help="YouTube video URL")

    parser.add_argument( "-o", "--output", type=str, default=None, help="Output path (leave blank for current directory)" )

    parser.add_argument( "-q", "--quality", type=str, default=None,
                        help="Video quality (e.g., 720p, 1080p). Leave blank for highest available quality" )

    args = parser.parse_args()
    if not args.url:
        print("You must provide a YouTube video URL.")
        exit(1)
    YouTubeDownloader(url=args.url, output_path=args.output, quality=args.quality).download()