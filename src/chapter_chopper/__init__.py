from pathlib import Path

from loguru import logger


def main() -> None:
    logger.info(f"Hello from chapter-chopper! {Path(__file__)}")
