from datetime import datetime

class Calendar(object):
    def __init__(self):
        self.event_list = list()

    def add_event(self,event):
        self.event_list.append(event)

    def current_event(self):
        [day,hour] = datetime.now().strftime('%d %H').split()
        temp_list = [x for x in self.event_list if str(x.day) == day and str(x.hour) == hour ]
        return temp_list