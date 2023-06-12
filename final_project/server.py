from translator import Translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    french = Translator.english_to_french(english_text=textToTranslate)
    return french

@app.route("/frenchToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english = Translator.french_to_english(french_text= textToTranslate )
    return english

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
