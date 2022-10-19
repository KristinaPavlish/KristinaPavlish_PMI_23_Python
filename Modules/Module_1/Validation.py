

import re

class Validation:
    @staticmethod
    def validate_name(function):
        def valid_str(booking, value):
            if any(map(str.isdigit, value)):
                raise ValueError("Can not contain digit.")
            return function(booking, value)
        return valid_str

    @staticmethod
    def validate_number_of_people(function):
        def is_natural(patient, item):
            try:
                if not int(item):
                    raise ValueError("Must contain natural.")
                if 0 > int(item) > 10:
                    raise ValueError("Must be in range 0 - 10")
            except ValueError:
                raise ValueError("Must contain natural.")
            item = int(item)
            return function(patient, item)
        return is_natural

    @staticmethod
    def decorator_time(function):
        def correct_time(patient, time):
            try:
                hour, minute = time.split(":")
                if not int(hour) or not int(minute) or len(hour) != 2 or len(minute) != 2:
                    raise ValueError("Time must be H:M")
            except ValueError:
                raise ValueError("Time must be H:M")
            return function(patient, time)
        return correct_time

    @staticmethod
    def decorator_hour(function):
        def correct_hour(patient, hour):
            try:
                if 00 > int(hour) > 24:
                    raise ValueError("Incorrect time")
            except ValueError:
                raise ValueError("Time must be integer")
            return function(patient, hour)
        return correct_hour

    @staticmethod
    def decorator_minute(function):
        def correct_minute(patient, minute):
            try:
                if 00 > int(minute) > 60:
                    raise ValueError("Incorrect time")
            except ValueError:
                raise ValueError("Time must be integer")
            return function(patient, minute)
        return correct_minute

    @staticmethod
    def validatePrice(func):
        def validatePriceWrapper(product, value):
            try:
                if not float(value):
                    raise ValueError("Price must be float")
                v = float(value)
                if re.match(r'[0-9]*\.[0-9]{2}', value):
                    raise ValueError("Price must have two digits after coma.")
            except ValueError:
                raise ValueError("Price must be float of int and must have two digits after coma!")
            return func(product, value)
        return validatePriceWrapper
