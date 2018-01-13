import requests

class Braian(object):

    def __init__(self):
        self.contactnumber=690890608
        self.BASE_PATH = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/da417be9-5a0f-4e02-972a-d16c59ee77f8?subscription-key=855fe00606ef48ecb4dafc6a30b92845&verbose=true&timezoneOffset=0&q="

    def _replace(self,a):
        return a.replace(' ',"%20")

    def _get_request(self, message):
        return requests.get(self.BASE_PATH+self._replace(message)).json()

    def _best_intent(self,answer):
        return answer['topScoringIntent']['intent']

    def _serve_message(self, answer):
        intent = self._best_intent(answer)
        if intent == "Signal":
            self._signal_message(answer)
        elif intent == "None":
            self._none_message(answer)
        elif intent == "Calendar.Add":
            self._calendaradd(answer)
        else:
            print("No idea :/")

    def _none_message(self, answer):
        printf("I don't understand, please try again")

    def _signal_message(self, answer):
        print("Sending SOS message to the number: ",self.contactnumber)

    def run(self):
        while(1):
            input_message = input()
            answer = self._get_request(input_message)
            self._serve_message(answer)
            print(self._best_intent(answer))
