from deep_translator import MyMemoryTranslator

class Translator:
    """
    A class that provides translation services between English and French.
    """

    def english_to_french(english_text):
        """
        Translates English text to French.

        Args:
            english_text (str): The text to translate.

        Returns:
            str: The translated text in French.
        """
        translator = MyMemoryTranslator(source='en', target='fr')
        if not english_text:
            return "Type a word or phrase in English."
        french_text = translator.translate(text=english_text)
        return french_text

    def french_to_english( french_text):
        """
        Translates French text to English.

        Args:
            french_text (str): The text to translate.

        Returns:
            str: The translated text in English.
        """
        translator = MyMemoryTranslator(source='fr', target='en')
        if not french_text:
            return "Type a word or phrase in French."
        english_text = translator.translate(text=french_text)
        return english_text
    """
This module provides functions for translating text between languages using various APIs.
"""

# print(Translator.english_to_french(english_text= "Hello"))