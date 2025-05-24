# YouTubeDownloader

A simple command-line tool to download YouTube videos effortlessly, selecting the desired resolution and output location.

## Features

- Download videos from YouTube using a URL.
- Choose from available video resolutions or default to the highest quality. Currently supports 360p only in most cases due to limitations in the `pytubefix` library.
- Specify an output directory, or save to the current directory by default.
- Display download completion details including video title, resolution, and file size.

## Requirements

- Python 3.6 or higher
- `pytubefix` library

## Installation

Make sure Python is installed. You can download necessary dependencies using:

```bash
pip install -r requirements.txt
```

## Usage
Run the downloader from the command line:

```bash
python youtube_downloader.py -u <YouTube_URL> [-o <Output_Path>] [-q <Quality>]
```

## Arguments
- `-u, --url`: (Required) Provide the YouTube video URL.
- `-o, --output`: (Optional) Specify the directory to save the video. Defaults to the current working directory if not provided.
- `-q, --quality`: (Optional) Set desired video quality, such as 720p or 1080p. Defaults to the highest available resolution.

## Example
```bash
python src/youtube_downloader.py -u https://www.youtube.com/watch?v=dQw4w9WgXcQ -o videos -q 360p
```

## How It Works
1. Initialize YouTubeDownloader with the URL, desired output path, and quality.
2. Fetch available resolutions and validate the quality input.
3. Download the video at the specified or highest possible quality.
4. Outputs completion details including file path, size, and other metadata.

## Error Handling
- Defaults to the highest quality if the specified resolution is unavailable.
- Requires URL input, displays an error message, and exits if missing.

## Disclaimer
This tool is intended for personal and educational purposes only. Ensure compliance with YouTube's terms of service when downloading videos.