class Event(object):
    def __init__(self,text,day,hour,minutes):
        self.text = text
        self.day=day
        self.hour=hour
        self.minutes=minutes
        self.last_printed_day = -1
