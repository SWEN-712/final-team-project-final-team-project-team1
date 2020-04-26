try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

SOURCE_LANGUAGE_OPTIONS = ['English', 'Spanish', 'French', 'Hindi']
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def ocr_core(filename, language):
    """
    This function will handle the core OCR processing of images.
    """
    import platform
    if platform.system() != 'Darwin':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename), lang=language)
    if not text:
        return "No text detected in the image"
    return text


def format_language(language):
    if language == SOURCE_LANGUAGE_OPTIONS[0]:
        return 'eng'
    elif language == SOURCE_LANGUAGE_OPTIONS[1]:
        return 'spa'
    elif language == SOURCE_LANGUAGE_OPTIONS[2]:
        return 'fra'
    elif language == SOURCE_LANGUAGE_OPTIONS[3]:
        return 'hin'
