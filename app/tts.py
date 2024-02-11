from gtts import gTTS
import os
msg = 'Welcome to Braille Buzz!'
tts = gTTS(text=msg, lang='en', slow=False)
tts.save("welcome.mp3")
os.system("groove welcome.mp3")