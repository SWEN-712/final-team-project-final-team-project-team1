try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
SOURCE_LANGUAGE_OPTIONS = ['English', 'Spanish', 'French', 'Hindi']

def allowed_file(filename):
    """
    Checks if file extension is allowed
    :param filename: name of file with extension
    :return: If extension is allowed or not
    """

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def ocr_core(filename, language):
    """
    This function extracts text from image
    """
    import platform
    if platform.system() != 'Darwin':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename), lang=language)
    if not text:
        return "No text detected in the image"
    return text


def format_language(language):
    """
    This function chooses source language
    :param language: source language
    :return: language chosen
    """

    if language == SOURCE_LANGUAGE_OPTIONS[0]:
        return 'eng'
    elif language == SOURCE_LANGUAGE_OPTIONS[1]:
        return 'spa'
    elif language == SOURCE_LANGUAGE_OPTIONS[2]:
        return 'fra'
    elif language == SOURCE_LANGUAGE_OPTIONS[3]:
        return 'hin'
