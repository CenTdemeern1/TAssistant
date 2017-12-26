from gtts import gTTS
import speechrec
from os import system as s

def hear():
    message=''
    while message != 'stop':
        speech = speechrec.speechrec()
        if speech is not None:
        	message = speech
        else:
            message = 'I could not process that request.'
        if __name__ == '__main__':
            tts=gTTS(text=message, lang='en')
            tts.save('C:/temp/tts.mp3')
            s('start /min cscript play.vbs //b //NoLogo')
        else:
            return message
            break

def say(message):
    tts=gTTS(text=message, lang='en')
    tts.save('C:/temp/tts.mp3')
    s('start /min cscript play.vbs //b //NoLogo')

if __name__ == '__main__':
    hear()
