import argparse
import os
import sys
from pathlib import Path

from loguru import logger

from chapter_chopper.split_to_chapters import (
    NoChaptersFoundError,
    split_pdf_by_chapters,
)


def default_download_dir() -> Path:
    # Determine the default Downloads directory based on the operating system
    if os.name == "nt":  # Windows
        default_download_dir = Path(os.getenv("USERPROFILE")) / "Downloads"
    else:  # macOS and Linux
        default_download_dir = Path.home() / "Downloads"

    return default_download_dir


def main():
    logger.info("Starting ChapterChopper CLI")
    parser = argparse.ArgumentParser(description="ChapterChopper CLI")
    parser.add_argument("input_file", help="Path to the input PDF file")
    parser.add_argument(
        "output_dir",
        help="Path to the output directory",
        nargs="?",
        default=default_download_dir(),
    )

    args = parser.parse_args()

    # Process the input_file
    input_file = Path(args.input_file)
    output_dir = Path(args.output_dir)

    assert input_file.exists(), f"File not found: {input_file}"

    try:
        logger.info(f"Processing {input_file} - Output Directory: {output_dir}")
        split_pdf_by_chapters(pdf_path=input_file, output_dir=output_dir)
    except NoChaptersFoundError as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    main()
