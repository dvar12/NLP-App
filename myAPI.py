
import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key('XogKnRwliDjWaufCpFz7xIyX8l4tkzjk8Y1BzpaC2NE')
    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response

    def ner(self,text):
       response=paralleldots.ner(text)
       return response

    def emotion(self,text):
       response=paralleldots.emotion(text)
       return response

