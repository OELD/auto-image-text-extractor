# Screenshot OCR Extractor

A simple Python tool that performs OCR (text recognition) on all images in a folder and saves the combined text into one file.

## Requirements

- Python 3.x
- Windows (for the .bat files)
- Tesseract OCR (installed automatically via `install.bat` if `winget` is available)

## Installation

Double-click `install.bat` to install Python dependencies and Tesseract OCR if you don't have them yet.

## Usage

Open Command Prompt and run:

```
run_ocr.bat C:\path\to\your\screenshots
```

Extracted text will be saved to `output/all_text.txt`.

## Project Structure

```
screenshot_ocr/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── ocr_processor.py
├── output/
├── install.bat
├── run_ocr.bat
├── requirements.txt
├── README.md
└── LICENSE
```

## License

MIT License.
