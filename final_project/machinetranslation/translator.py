import json
import os
from deep_translator import MyMemoryTranslator


class Translator:
    def englishToFrench(english_text):
        translator = MyMemoryTranslator(source='en', target='fr')
        if english_text == "" or english_text is None:
            return "Type a word or phrase in English."
        frenchText = translator.translate(english_text)
        return frenchText
        
    def FrenchToEnglish(french_text):
        translator = MyMemoryTranslator(source='fr', target='en')
        if french_text == "" or french_text is None:
            return "Type a word or phrase in French."
        englishText = translator.translate(text=french_text)
        return englishText
    
