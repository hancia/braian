import requests
from Calendar import Calendar
from event import Event
class Braian(object):

    def __init__(self):
        self.contactnumber=610890608
        self.BASE_PATH = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/da417be9-5a0f-4e02-972a-d16c59ee77f8?subscription-key=855fe00606ef48ecb4dafc6a30b92845&verbose=true&timezoneOffset=0&q="
        self.calendar = Calendar()

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

        drug_list = self.calendar.current_event()

        for i in drug_list:
            print("Please take",i.text," now")

    def _none_message(self, answer):
        print("I don't understand, please try again")

    def _signal_message(self, answer):
        print("Sending SOS message to the number: ",self.contactnumber)

    def _calendaradd(self, answer):
        try:
            for i in answer['entities']:
                type = str(i['type'])
                if type == 'time':
                    time = i['entity']
                elif type == "drug":
                    drug = i["entity"]
                elif type == "day":
                    day = i["entity"]
                elif type == "minutes":
                    minutes = i["entity"]

            event = Event(drug,day,time,minutes)
            self.calendar.add_event(event)
            print("I added your reminder")
        except:
            print("Blad wiadomosci")


    def run(self):
        print("Hi, how can I help you?")
        while(1):
            input_message = input()
            answer = self._get_request(input_message)
            self._serve_message(answer)