import pyttsx3
name = "Jarvis"
engine = pyttsx3.init()


class Speaker :
    def __init__(self):
        self.name = "Jarvis"
        self.engine = pyttsx3.init()
        self.setCurrentVoice()

    def setCurrentVoice(self):
        voices = self.getVoice()
        self.engine.setProperty('voice', voices[1].id)

    def playAllVoices(self):
        voices = self.getVoice()
        for voice in voices:
            self.engine.setProperty('voice', voice.id)
            self.engine.say("This is a test")
            self.engine.runAndWait()
        
    def getVoice(self):
        # get all available voices
        voices = self.engine.getProperty('voices')
        print(voices)
        return voices

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    def run(self):
        self.engine.runAndWait()
    def stop(self):
        self.engine.stop()
    def isSpeaking(self):
        return self.engine.isBusy()
