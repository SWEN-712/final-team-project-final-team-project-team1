import os
from flask import Flask, render_template, request

# import OCR and Translation modules
import ocr_core
import translator

# define a folder to store and later serve the images
UPLOAD_FOLDER = 'static/uploads/'

# allow files of a specific type
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
            return render_template('upload.html', msg='No file selected',
                                   source_languages=ocr_core.SOURCE_LANGUAGE_OPTIONS,
                                   target_languages=translator.TARGET_LANGUAGE_OPTIONS)
        file = request.files['file']
        lang = request.form.get('source_languages')
        target_lang = request.form.get('target_languages')

        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected',
                                   source_languages=ocr_core.SOURCE_LANGUAGE_OPTIONS,
                                   target_languages=translator.TARGET_LANGUAGE_OPTIONS)

        if file and ocr_core.allowed_file(file.filename):
            # call the OCR function on it
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            lang = ocr_core.format_language(lang)
            extracted_text = ocr_core.ocr_core(file, lang)
            if target_lang != 'None':
                target_lang = translator.format_language(target_lang)
                extracted_text = translator.translate(extracted_text, target_lang)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   source_languages=ocr_core.SOURCE_LANGUAGE_OPTIONS,
                                   target_languages=translator.TARGET_LANGUAGE_OPTIONS,
                                   img_src=os.path.join(app.config['UPLOAD_FOLDER'], file.filename),
                                   )
    elif request.method == 'GET':
        return render_template('upload.html', source_languages=ocr_core.SOURCE_LANGUAGE_OPTIONS,
                               target_languages=translator.TARGET_LANGUAGE_OPTIONS)


if __name__ == '__main__':
    app.run()
