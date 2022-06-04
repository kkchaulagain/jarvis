class ActionAnalyzer:
    def __init__(self, query):
        self.query = query
        self.query_list = self.query.lower().split()
    
    # use gpt3 to generate text
    def generateText(self):
        pass
    