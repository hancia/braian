from datetime import datetime

class Calendar(object):
    def __init__(self):
        self.event_list = list()

    def add_event(self,event):
        self.event_list.append(event)

    def current_event(self):
        [day, hour, minutes] = datetime.now().strftime('%d %H %M').split()
        temp_list = [x for x in self.event_list if  str(x.hour) == str(hour) and str(x.minutes) == str(minutes) and str(day) != str(x.last_printed_day)]
        for i in temp_list:
            i.last_printed_day = str(day)
        return temp_list