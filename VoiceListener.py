import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont
import time

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('What would you like to translate to British Sign Language?')
        w = Image.new("RGB", (2000, 1000), "white")
        x = ImageDraw.Draw(w)
        font = ImageFont.truetype('Arial.ttf', 45)
        x.text((830, 10), "What would you like to translate to British Sign Language?", font=font, fill=(100, 149, 237))
        w.show()
        time.sleep(2)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("No words detected.")
        w = Image.new("RGB", (2000, 1000), "white")
        x = ImageDraw.Draw(w)
        font = ImageFont.truetype('Arial.ttf', 45)
        x.text((830, 10), "No words detected.", font=font, fill=(100, 149, 237))
        w.show()
        time.sleep(2)
        exit(999)


print('/Users/DoDoBird/Desktop/APP/Actions/%s' % "awo")
