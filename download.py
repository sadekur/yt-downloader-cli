#!/usr/bin/env python3
import argparse
import sys

from yt_dlp import YoutubeDL

OUTPUT_DIR = "downloads"


def build_format(quality: str) -> str:
    if quality == "best":
        return "bestvideo+bestaudio/best"
    if quality == "audio":
        return "bestaudio/best"
    height = quality.rstrip("p")
    return f"bestvideo[height<={height}]+bestaudio/best[height<={height}]"


def download(url: str, quality: str) -> None:
    ydl_opts = {
        "format": build_format(quality),
        "outtmpl": f"{OUTPUT_DIR}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "noplaylist": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> None:
    parser = argparse.ArgumentParser(description="Download a YouTube video at a chosen quality.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--quality",
        default="720p",
        help="Target quality: e.g. 360p, 480p, 720p, 1080p, best, audio (default: 720p)",
    )
    args = parser.parse_args()

    try:
        download(args.url, args.quality)
    except Exception as exc:
        print(f"Download failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
