import os
from flask import Flask, render_template, request

# import our OCR function
from ocr_core import ocr_core

# define a folder to store and later serve the images
UPLOAD_FOLDER = 'static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
LANGUAGE_OPTIONS = ['English', 'Spanish', 'French', 'Hindi']
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def format_language(language):
    if language == LANGUAGE_OPTIONS[0]:
        return 'eng'
    elif language == LANGUAGE_OPTIONS[1]:
        return 'spa'
    elif language == LANGUAGE_OPTIONS[2]:
        return 'fra'
    elif language == LANGUAGE_OPTIONS[3]:
        return 'hin'


# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')


# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected', languages=LANGUAGE_OPTIONS)
        file = request.files['file']
        lang = request.form.get('languages')
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected', languages=LANGUAGE_OPTIONS)

        if file and allowed_file(file.filename):
            # call the OCR function on it
            lang = format_language(lang)
            extracted_text = ocr_core(file, lang)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename,
                                   languages=LANGUAGE_OPTIONS
                                   )
    elif request.method == 'GET':
        return render_template('upload.html', languages=LANGUAGE_OPTIONS)


if __name__ == '__main__':
    app.run()
