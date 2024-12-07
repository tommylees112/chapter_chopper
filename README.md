# 📚 Chapter Chopper

Split your PDFs into chapters automatically! Perfect for organizing your digital library.

## 🎯 What it does

Chapter Chopper takes your PDF books and intelligently splits them into separate files by chapter, using the PDF's table of contents. No more endless scrolling to find the chapter you want!

## 🚀 Installation

```bash
uv run pipx install -e .
```

## 💡 Usage

### Command Line

```bash
chapter-chopper "path/to/your/book.pdf" [output_directory]
```

- If no output directory is specified, files will be saved to your Downloads folder
- Creates a new folder with the book's name
- Generates individual PDF files for each chapter
- Files are named with chapter numbers and titles (e.g., `1_introduction.pdf`)

### Example

```bash
chapter-chopper "clean_code.pdf"
```

This will:
1. Create a folder `clean_code` in your Downloads directory
2. Split the book into chapters
3. Save files like:
   - `1_clean_code.pdf`
   - `2_meaningful_names.pdf`
   - `3_functions.pdf`
   ...

## ✨ Features

- 📑 Automatic chapter detection from PDF table of contents
- 📁 Organized output with book-specific folders
- 🔄 Handles nested chapters and sub-sections
- 💫 Clean, readable chapter filenames
- 🎯 Simple command-line interface

## 🛠️ Requirements

- Python ≥ 3.12
- PyPDF
- Loguru

## 📝 License

MIT License

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements

## 🙋‍♂️ Author

Tommy Lees - [thomas.lees112@gmail.com]

