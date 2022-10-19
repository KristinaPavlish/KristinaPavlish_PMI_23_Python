from datetime import datetime
class Decorator:
    @staticmethod
    def decorator_integer(function):
        def is_integer(patient, number):
            try:
                if int(number) and int(number) >= 0:
                    raise ValueError("Must contain integers.")
            except ValueError:
                raise ValueError("Must contain integers.")
            return function(patient, number)

        return is_integer

    @staticmethod
    def decorator_natural(function):
        def is_natural(patient, item):
            try:
                if not int(item):
                    raise ValueError("Must contain natural.")
                if int(item) <= 0:
                    raise ValueError("Must contain natural.")
            except ValueError:
                raise ValueError("Must contain natural.")
            item = int(item)
            return function(patient, item)

        return is_natural

    @staticmethod
    def decorator_word(function):
        def is_only_letter(patient, string):
            string = string.title()
            try:
                if not string.isalpha():
                    raise ValueError("Must contain only letter.")
            except ValueError:
                raise ValueError("Must contain only letter.")
            return function(patient, string)
        return is_only_letter

    @staticmethod
    def decorator_time(function):
        def correct_time(patient, time):
            time_format = "%H:%M:%S"
            try:
                datetime.strptime(time, time_format)
            except ValueError:
                raise ValueError("Time must be H:M:S")
            return function(patient, time)

        return correct_time

    @staticmethod
    def decorator_date(function):
        def correct_date(patient, date):
            date_format = "%d/%m/%Y"
            try:
                if not datetime.strptime(date, date_format):
                    raise ValueError("Time must be d/m/Y")
            except ValueError:
                raise ValueError("Time must be d/m/Y")
            return function(patient, date)

        return correct_date

    @staticmethod
    def validateFileName():
        def validateFileNameDecorator(func):
            def validateFileNameWrapper(L, filename):
                if not filename:
                    raise ValueError("Incorrect filename.")
                return func(L, filename)

            return validateFileNameWrapper

        return validateFileNameDecorator

    @staticmethod
    def validate_input(func):
        def valid_input(arg):
            while True:
                try:
                    func(arg)
                    break
                except ValueError as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except AttributeError as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except NameError as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except FileNotFoundError as e:
                    print(e)
                    print("Try one more time!")
                    continue

        return valid_input