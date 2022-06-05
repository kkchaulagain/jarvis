import openai
import os
FINETUNEDMODEL ='davinci:ft-personal-2022-06-05-08-33-20'
APIKEY = "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"
class Davinci :
    def __init__(self):
        self.ai_model = FINETUNEDMODEL
        self.setApiKey(key=APIKEY)

    def setApiKey (self, key) :
        #set the api key
        openai.api_key = key
    
    def analyze(self,query):
        completion = openai.Completion.create(
                model=self.ai_model,
                prompt=query,
                temperature=0.7,
                stop='###',
                max_tokens=300,
        )
        if(completion['choices'][0]['text']):
           completion['choices'][0]['text']
           return completion['choices'][0]['text']
        else:
           print("Sorry, I don't know what you mean")
        
        return False