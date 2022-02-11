import pyttsx3
# Super simple use of pyttsx3; allows me to play text simultanously
# gtts allows me to store text as an mp3 file

engine = pyttsx3.init()
engine.say("Yay, this works!")
engine.runAndWait()