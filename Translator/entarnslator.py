from googletrans import Translator

def translate_text(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest='en')
    return translation.text

text = input("Enter the text to translate: ")
translated_text = translate_text(text)
print("Translated text: ", translated_text)
