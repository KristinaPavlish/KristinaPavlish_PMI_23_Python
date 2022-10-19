"""Створити клас Booking, який містить такі поля
 1. Name (Тільки літери)
 2. NoOfPeople (1-10)
 3. StartTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)).
 4. EndTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)). Min: StartTime.
 5. Price (Число з 2 знаками після коми)
"""
from Time import Time
from Validation import Validation

class Booking:
    def __init__(self, name_ = None, no_of_people_ = None, start_time_ = None, end_time_ = None):
        self.name = name_
        self.no_of_people = no_of_people_
        self.start_time = start_time_
        self.end_time = end_time_

    @property
    def name(self):
        return self.name

    @property
    def no_of_people(self):
        return self.no_of_people

    @property
    def start_time(self):
        return self.start_time

    @property
    def end_time(self):
        return self.end_time

    @property
    def price(self):
        return self.price

    @Validation.validate_name
    @name.setter
    def name(self, name_):
        self.name = name_

    @Validation.validate_number_of_people
    @no_of_people.setter
    def no_of_people(self, no_of_people_):
        self.no_of_people = no_of_people_

    @Validation.decorator_time
    @start_time.setter
    def start_time(self, start_time_):
        self.start_time = start_time_

    @Validation.decorator_time
    @end_time.setter
    def end_time(self, end_time_):
        self.end_time = end_time_

    @price.setter
    @Validation.validatePrice
    def price(self, price_):
        self.price = price_

    def input_booking(self):
        while True:
            try:
                first_time = Time(0, 0)
                second_time = Time(0, 0)
                self.name = input("Enter name: ")
                self.no_of_people = input("Enter no of people: ")
                self.start_time = first_time.input_time(self.start_time)
                self.end_time = second_time.input_time(self.start_time)
                self.price = input("Enter price: ")
            except ValueError as e:
                print(e)
                print("Try one more time!")
                continue

    def __str__(self):
        return "Name: {0}, No of people: {1}, start time: {2}, End time: {3}, price: {4}" \
            .format(
            self.name,
            self.no_of_people,
            self.start_time,
            self.end_time,
            self.price,
        )
