from pathlib import Path

from loguru import logger
from pypdf import PdfReader, PdfWriter

from chapter_chopper.extract_toc import extract_toc


def split_pdf_by_chapters(pdf_path: Path, output_dir: Path) -> None:
    """
    Splits a PDF file into separate chapters based on the table of contents (TOC).

    Args:
        pdf_path (Path): The path to the PDF file to be split.
        output_dir (Path): The directory where the split chapter PDFs will be saved.

    Returns:
        None

    This function reads the PDF file, extracts the table of contents to determine the chapters,
    and then splits the PDF into separate files for each chapter. The output files are saved
    in the specified output directory with filenames based on the chapter titles.
    """
    logger.info(f"Splitting PDF: {pdf_path}")

    # Extract the book title
    book_title = pdf_path.stem.replace(" ", "_").lower()
    logger.info(f"Book Title: {book_title}")

    # read the pdf document and get the chapters
    reader = PdfReader(pdf_path)
    chapters = extract_toc(pdf_path)
    logger.info(f"{len(chapters)} Chapters: {chapters[:5]}")

    book_directory = output_dir / book_title
    book_directory.mkdir(exist_ok=True)

    # Split the PDF into chapters from the start page to the end page
    for i, (title, start_page) in enumerate(chapters):
        # the end page is the start page of the next chapter (i+1)
        # chapters = [(title, start_page), ...]
        end_page = chapters[i + 1][1] if i + 1 < len(chapters) else len(reader.pages)

        # create a new PdfWriter for the chapter
        writer = PdfWriter()
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        chapter_title = title.replace(" ", "_").lower()
        output_file = book_directory / f"{i + 1}_{chapter_title}.pdf"

        # write the output pdf
        with open(output_file, "wb") as f:
            writer.write(f)

        logger.info(f"Saved: {output_file}")
