# yt-downloader-cli

Simple command-line YouTube video downloader for local/personal use. Uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) + ffmpeg.

## Requirements

- Python 3
- ffmpeg (`sudo apt install ffmpeg`)

## Setup

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

## Usage

```bash
./.venv/bin/python download.py "https://www.youtube.com/watch?v=VIDEO_ID" --quality 720p
```

`--quality` accepts: `360p`, `480p`, `720p`, `1080p`, `best`, `audio` (default: `720p`).

Downloaded files are saved to `downloads/`.
