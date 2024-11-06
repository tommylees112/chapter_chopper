from pathlib import Path

from loguru import logger
from pypdf import PdfReader


def get_chapter_info(item: dict, reader: PdfReader) -> tuple[str, int]:
    """extract the chapter title and page number from the item (dict object read from reader.outline).

    Args:
        item (dict): _description_
        reader (PdfReader): _description_

    Returns:
        tuple[str, int]: _description_
    """
    title = item.get("/Title")
    page_num = reader.get_destination_page_number(item)

    return (title, page_num)


def extract_toc(pdf_path: Path) -> list[tuple[str, int]]:
    """
    Extracts the table of contents (TOC) from a PDF file.

    Args:
        pdf_path (Path): The path to the PDF file.

    Returns:
        list[tuple[str, int]]: A list of tuples where each tuple contains a chapter title (str)
                               and its corresponding page number (int).

    Example:
        >>> toc = extract_toc(Path("example.pdf"))
        >>> print(toc)
        [('Chapter 1', 1), ('Chapter 2', 5), ('Chapter 3', 10)]

    Notes:
        - This function uses the PdfReader to read the PDF and extract the TOC.
        - The TOC is expected to be in the form of a list of dictionaries or nested lists.
        - Each dictionary should contain a "/Title" key for the chapter title.
        - The page number is determined using the get_destination_page_number method of PdfReader.
    """
    reader = PdfReader(pdf_path)
    toc = reader.outline
    logger.info(f"Table of Contents: {len(toc)}")

    chapters: list[tuple[str, int]] = []
    for item in toc:
        # Get subitems if the item is a list (sub chapters)
        if isinstance(item, list):
            for subitem in item:
                if isinstance(subitem, dict):
                    (title, page_num) = get_chapter_info(subitem, reader)
                    chapters.append((title, page_num))

        # Process the item if it is a dictionary (a single chapter)
        elif isinstance(item, dict):
            (title, page_num) = get_chapter_info(item, reader)
            chapters.append((title, page_num))

    return chapters
