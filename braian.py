import requests

class Braian(object):

    def __init__(self):
        self.BASE_PATH = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/da417be9-5a0f-4e02-972a-d16c59ee77f8?subscription-key=855fe00606ef48ecb4dafc6a30b92845&verbose=true&timezoneOffset=0&q="

    def _replace(self,a):
        return a.replace(' ',"%20")

    def _get_request(self, message):
        return requests.get(self.BASE_PATH+self._replace(message)).json()

    def _best_intent(self,answer):
        return answer['topScoringIntent']['intent']

    def run(self):
        while(1):
            input_message = input()
            answer = self._get_request(input_message)
            print(self._best_intent(answer))


