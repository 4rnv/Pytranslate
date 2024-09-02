from flask import Flask, render_template, request, send_file
from app import translate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.jinja')

@app.route('/translate', methods=['POST'])
def translate_post():
    userinput_text = request.form['query']
    userinput_lang = request.form['lang']
    translated_text, filename = translate(userinput_text,userinput_lang)
    #return translated_text
    return {'translated_text': translated_text, 'filename': filename}

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)