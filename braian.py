import requests
from Calendar import Calendar
from event import Event
import pyttsx3

class Braian(object):

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',120)
        self.engine.setProperty('volume',0.9)

        self.contactnumber=610890608
        self.BASE_PATH = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/da417be9-5a0f-4e02-972a-d16c59ee77f8?subscription-key=855fe00606ef48ecb4dafc6a30b92845&verbose=true&timezoneOffset=0&q="
        self.calendar = Calendar()

    def say(self, text):
        self.engine.say(text)
        print(text)
        self.engine.runAndWait()

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
        elif intent == "Weather":
            self._checkweather(answer)
        else:
            self.say("No idea")

        drug_list = self.calendar.current_event()

        for i in drug_list:
            self.say("Please take {} now".format(i.text))


    def _checkweather(self,answer):
        weather = requests.get('http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22').json()
        temp=str(int(weather['main']['temp'])-273)
        wind=weather['wind']['speed']
        self.say("Today its {} degrees and the wind speed is {} kilometers per hour".format(temp,wind))

    def _none_message(self, answer):
        self.say("I don't understand, please try again")

    def _signal_message(self, answer):
        self.say("Sending SOS message to the number: ",self.contactnumber)

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
            self.say("I added your reminder")
        except:
            self.say("Bad message")


    def run(self):
        while(1):
            self.say("Hi")
            input_message = input()
            answer = self._get_request(input_message)
            self._serve_message(answer)