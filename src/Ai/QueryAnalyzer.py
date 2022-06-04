class QueryAnalyzer:

    def __init__(self, query):
        self.query = query
        self.query_list = self.query.lower().split()
        self.query_list_len = len(self.query_list)
        self.hotWords = [
            {
                "word": "jarvis",
                "command": "reply",
                "type": "query"
            },{

                "word": "introduce",
                "command": "introduce",
                "type": "command"
            },
             {
                "word": "greetings",
                "command": "greet",
                 "type": "query"
            },
            {
                "word": "listen",
                "command": "listen",
                "type": "query"
            },
            {
                "word": "bro",
                "command": "reply",
                "type": "query"
            },
            {
                "word": "time",
                "command": "time",
                "type": "query"
                
            },
            {
                "word": "deploy",
                "command": "deploy",
                 "type": "command"
            }
        ]
        self.command = 'query'
        self.analyze()
        

    def analyze(self):
        for word in self.hotWords:
            if word["word"] in self.query_list:
                self.command = word["command"]
                self.type = word["type"]
                return self.command

    def getCommand(self):
        print (self.command)
        return self.command