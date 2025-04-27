import os
import sys
from ocr_processor import perform_ocr

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <input_folder>")
        sys.exit(1)
    input_folder = sys.argv[1]
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'all_text.txt')

    print(f"Processing images in {input_folder}...")
    extracted = perform_ocr(input_folder)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(extracted)

    print(f"OCR complete. Extracted text saved to {output_file}")

if __name__ == '__main__':
    main()
