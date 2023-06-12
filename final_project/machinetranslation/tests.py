import unittest
from translator import Translator

def test_french_to_english(self):
        translate = Translator()
        self.assertEqual(('Bonjour'), 'Hello')
        self.assertNotEqual(translate.englishToFrench("None"), '')

def test_english_to_french(self):
  translate = Translator()

  self.assertEqual(translate.FrenchToEnglish('Hello'), 'Bonjour')
    
  self.assertNotEqual(translate.FrenchToEnglish("None"), '')

if __name__ == '__main__':
    unittest.main()