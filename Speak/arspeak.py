from googletrans import Translator
from gtts import gTTS
import os

def translate_and_speak(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest='ar')
    translated_text = translation.text

    tts = gTTS(text=translated_text, lang='ar')
    tts.save("translation.mp3")
    os.system("start translation.mp3")

text = input("Enter the text to translate and speak: ")
translate_and_speak(text)
