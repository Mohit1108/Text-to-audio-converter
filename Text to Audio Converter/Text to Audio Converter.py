"""
Welcome to Coder Mohit
Author - Mohit Goyal
Project Name - Text to Audio Converter
Source Code Link - www.TechyCodes.tech

"""
# Import Necessary modules & Libraries.

from gtts import gTTS
# pip install gtts
from playsound import playsound
# install by pip install playsound

# now come to coding
audio = 'speech.mp3'

language = 'en'
# Here i have set the language that i want to convert the text into audio.

Text = "This Code is Available on TechyCodes.tech Website. Check now"
# This is my text that i want to convert in the Audio.

sp = gTTS(text=Text, lang=language, slow=False)
sp.save(audio)
playsound(audio)

# So in line 29  i have save the audio and in line 31 i have to play that sound.
# now Run this Code ....
# now i have to change this audio,












