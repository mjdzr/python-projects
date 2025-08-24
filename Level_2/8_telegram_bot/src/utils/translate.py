# translator_module.py

from langdetect import detect, LangDetectException
from googletrans import Translator

def detect_language(text):
    """
    Detects the language of the given text.

    Returns the detected language code if successful, or
    raises an exception in case of an error.
    """
    try:
        language = detect(text)
        return language

    except LangDetectException as e:
        print(f"Language detection error: {str(e)}")
        return None

def translate_text(text, target_lang='en'):
    """
    Translates the given text to the target language using googletrans.
    
    Returns the translated text if successful, or raises an exception in case of an error.
    """
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_lang)
        return translation.text

    except Exception as e:
        print(f"Translation error: {str(e)}")
        return None
