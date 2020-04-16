try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename, language):
    """
    This function will handle the core OCR processing of images.
    """
    import platform
    if platform.system() != 'Darwin':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename), lang=language)
    return text

# print(ocr_core('FlaskApp\images\ocr_example_1.jpg'))
