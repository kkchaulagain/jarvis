import speech_recognition as sr

class Ear :
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.pause_threshold = 0.5
        self.listen_threshold = 5
        self.response_threshold = 0.5
        self.recognizer.pause_threshold = self.pause_threshold
        self.recognizer.listen_threshold = self.listen_threshold

        # set amnount of seconds to wait for speech to be recognized
        self.recognizer.response_threshold = self.response_threshold
      


    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)
            try:
                query =  self.recognizer.recognize_google(audio, language='en-in')
                print("You said : {}".format(query))
                return query
            except Exception as e:
                print("Google Speech Recognition could not understand audio")
        return "None"