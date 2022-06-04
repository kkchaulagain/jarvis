# import speaker class from src/lib/speaker.py

from src.Ai.Brain import Brain 
class Jarvice :
    def __init__(self):
        self.name = self.myName()
        self.brain = Brain()

    def myName(self):
     return "Jarvis"

    def greet(self):
        self.brain.greet()

    #  listen to awakened state
    def wakeUp(self):
       self.brain.wakeUp()
