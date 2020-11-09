from gtts import gTTS
import os


fh = open("test.txt", "r")
myText = fh.read().replace("\n", " ")
#myText = "Knight"+"C"+"4"+"to"+"Dee"+"7"

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("Output.mp3")
fh.close()
os.system("start Output.mp3")