import requests
import time
import os
from dotenv import load_dotenv
from docx import Document
load_dotenv()
api_key = os.environ['APIKEY']
endpoint = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'

def save_to_docx(translated_text):
    timestamp = int(time.time()*1000000)
    filename = f"{timestamp}.docx"
    document = Document()
    document.add_paragraph(translated_text)
    document.save(filename)
    return filename

def translate(text, lang):
    if not text or not lang:
        raise ValueError("Text and target language are required")

    try:
        response = requests.post(
            f"{endpoint}&to={lang}",
            json=[{'Text': text}],
            headers={
                'Ocp-Apim-Subscription-Key': api_key,
                'Ocp-Apim-Subscription-Region': 'southeastasia',
                'Content-Type': 'application/json'
            }
        )

        response.raise_for_status()  # Raise an error for bad responses
        translated_text = response.json()[0]['translations'][0]['text']
        filename = save_to_docx(translated_text)
        return translated_text, filename

    except requests.exceptions.RequestException as error:
        print('Error translating text:', error)
        return None

#print(translate("Hello world", 'de'))