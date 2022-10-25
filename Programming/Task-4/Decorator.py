from datetime import datetime
from Error import PatientIdIncorrect, NameIncorrect, DateIncorrect, TimeIncorrect, DurationInMinuteIncorrect, DepartmentIncorrect, DoctorNameIncorrect
class Decorator:
    @staticmethod
    def decorator_time_in_minute(function):
        def is_natural(patient, item):
            try:
                if not int(item):
                    raise DurationInMinuteIncorrect
                if int(item) <= 0:
                    raise DurationInMinuteIncorrect
            except ValueError:
                raise DurationInMinuteIncorrect
            item = int(item)

        return is_natural

    @staticmethod
    def decorator_id(function):
        def is_natural(patient, item):
            try:
                if not int(item):
                    raise PatientIdIncorrect
                if int(item) <= 0:
                    raise PatientIdIncorrect
            except ValueError:
                raise PatientIdIncorrect
            item = int(item)

        return is_natural

    @staticmethod
    def decorator_patient_name(function):
        def is_only_letter(patient, string):
            string = string.title()
            try:
                string = string.title()
                if not string.isalpha():
                    raise NameIncorrect
            except ValueError:
                raise NameIncorrect
        return is_only_letter

    @staticmethod
    def decorator_doctor_name(function):
        def is_only_letter(patient, string):
            string = string.title()
            try:
                string = string.title()
                if not string.isalpha():
                    raise DoctorNameIncorrect
            except ValueError:
                raise DoctorNameIncorrect
        return is_only_letter

    @staticmethod
    def decorator_department(function):
        def is_only_letter(patient, string):
            string = string.title()
            try:
                string = string.title()
                if not string.isalpha():
                    raise DepartmentIncorrect
            except ValueError:
                raise DepartmentIncorrect
        return is_only_letter

    @staticmethod
    def decorator_time(function):
        def correct_time(patient, time):
            try:
                time = datetime.strptime(time, "%H:%M:%S")
            except ValueError:
                raise ValueError("Time: ", time, " does not match format %H:%M:%S")

        return correct_time

    @staticmethod
    def decorator_date(function):
        def correct_date(patient, date):
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Date: ", date, " does not match format %Y-%m-%d")

        return correct_date

    @staticmethod
    def decorator_word(function):
        def is_only_letter(patient, string):
            string = string.title()
            try:
                if not string.isalpha():
                    raise ValueError("Must contain only letter.")
            except ValueError:
                raise ValueError("Must contain only letter.")
        return is_only_letter

    @staticmethod
    def decorator_integer(function):
        def is_integer(patient, number):
            try:
                if int(number) and int(number) >= 0:
                    raise ValueError("Must contain integers.")
            except ValueError:
                raise ValueError("Must contain integers.")

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

        return is_natural


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
    def validate_inp(function):
        def validate_inpWrapper(m):
            while True:
                try:
                    function(m)
                    break
                except PatientIdIncorrect as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except NameIncorrect as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except DateIncorrect as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except TimeIncorrect as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except DurationInMinuteIncorrect as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except DepartmentIncorrect as e:
                    print(e)
                    print("Try one more time!")
                    continue
                except DoctorNameIncorrect as e:
                    print(e)
                    print("Try one more time!")
                    continue
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
        return validate_inpWrapper
