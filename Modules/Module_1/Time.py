"""Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)"""

from Validation import Validation


class Time:
    def __init__(self, hour_, minute_):
        self.hour = hour_
        self.minute = minute_

    @property
    def hour(self):
        return self.hour

    @Validation.decorator_hour
    @hour.setter
    def hour(self, hour_):
        self.hour = hour_

    @property
    def minute(self):
        return self.minute

    @Validation.decorator_minute
    @minute.setter
    def minute(self, minute_):
        self.minute = minute_

    def input_time(self, time):
        self.hour = input("Enter hour: ")
        self.minute = input("Enter minute: ")
        time = self.hour + ":" + self.minute
        return time