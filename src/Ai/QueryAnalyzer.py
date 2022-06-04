class QueryAnalyzer:

    def __init__(self, query):
        self.query = query
        self.query_list = self.query.lower().split()
        self.query_list_len = len(self.query_list)
        self.hotWords = [
            {
                "word": "jarvis",
                "command": "reply",
            },
             {
                "word": "greetings",
                "command": "greet",
            },
            {
                "word": "listen",
                "command": "listen",
            },
            {
                "word": "bro",
                "command": "greet",
            },
            {
                "word": "time",
                "command": "time",
                
            },
            {
                "word": "deploy",
                "command": "deploy",
            }
        ]
        self.command = 'query'
        self.analyze()
        

    def analyze(self):
        for word in self.hotWords:
            if word["word"] in self.query_list:
                self.command = word["command"]
                return self.command

    def getCommand(self):
        print (self.command)
        return self.command