from src.lib.Ear import Ear
from src.lib.Speaker import Speaker
from src.Ai.QueryAnalyzer import QueryAnalyzer
from src.lib.assistant.GitAssistant import GitAssistant
import datetime

class Brain :

    def deploy(self):
        assistant = GitAssistant(self)
        self.say("Deploying...")
        assistant.deploy()
        self.say("Deployed!")

    def __init__(self) -> None:
        self.ear = Ear()
        self.mouth = Speaker()
    
    def think(self, query) :
        self.query = query
        self.analyzer = QueryAnalyzer(query)
        action = self.analyzer.getCommand()
        # check if query is a command
        if action == "greet" :
            return self.greet()
        elif action == "time" :
            return self.sayTime()
        elif action == "deploy" :
            return self.deploy()
        elif action == "reply" :
            self.say("Yes sir!")
        else :
            return self.executeQuery(self.query)

    def isCommand(self, query) :
        if query.startswith("jarvis") :
            return True
        else :
            return False

    def wakeUp(self):
        self.greet()
        while True:
            sleep =  self.listenForCommand()
            if sleep :
                break


    def sleep(self) :
        print("Sleeping...")
        return True

    def say(self, query) :
        self.mouth.say(query)
        return False

    def executeCommand(self, query) :
        if query.startswith("jarvis sleep") :
           return self.sleep()
        elif query.startswith("jarvis say") :
            return self.say(query)
        
    
    def executeQuery(self, query) :
        # get the query from the user
        # query = self.takeCommand()
        self.say("You said: " + query)

    def findMonth(self,monthNumber):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return months[monthNumber-1]

    def findTimeOfDay(self,currenttime):
        hour = currenttime.hour
        if (hour < 12):
            time = "morning"
        elif (hour < 18):
            time = "afternoon"
        else:
            time = "evening"
        return time

    def findTime(self,currenttime):
        # get Its current hour and minute
        hour = currenttime.hour
        minute = currenttime.minute
        #AM or PM
        if (hour < 12):
            time = "AM"
        else:
            time = "PM"
        #convert to 12 hour format
        if (hour > 12):
            hour -= 12
        elif (hour == 0):
            hour = 12
        #convert minutes to a readable format
        if (minute < 10):
            minute = "0"+str(minute)
        else:
            minute = str(minute)
        return str(hour) + ":" + str(minute) + " " + time


    def getGreetingText(self):
        #  get current time
        currentTime = datetime.datetime.now()
        month = self.findMonth(currentTime.month)
        year = currentTime.year
        time = self.findTime(currentTime)

        greeting = "Good "+ self.findTimeOfDay(currentTime)+','
        greeting += " it is "+ time +'.'
        greeting += " Today is "+ month +" "+ str(currentTime.day) +", "+ str(year) +"."
        greeting += " How can I help you?"
        return greeting

    def greet(self):
        self.say(self.getGreetingText())

    def sayTime(self):
        # get current time
        currentTime = datetime.datetime.now()
        time = self.findTime(currentTime)
        self.say("It is "+ time +'.')

    def listenForCommand(self):
        query = self.ear.listen()
        if(query == 'None'):
            return False
        return self.think(query)
