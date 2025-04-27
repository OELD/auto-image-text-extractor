import os
from PIL import Image
import pytesseract

def perform_ocr(input_folder):
    texts = []
    for root, _, files in os.walk(input_folder):
        for fname in files:
            if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                path = os.path.join(root, fname)
                try:
                    img = Image.open(path)
                    text = pytesseract.image_to_string(img)
                    texts.append(f"--- {fname} ---\n{text}\n")
                except Exception as e:
                    texts.append(f"--- {fname} ---\nError: {e}\n\n")
    return ''.join(texts)
