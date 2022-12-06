from Decorator import Decorator


class Patient(object):
    def __init__(self, **kwargs):
        for (prop, default) in kwargs.items():
            setattr(self, prop, kwargs.get(prop, default))

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    @Decorator.decorator_id
    def patient_id(self, value):
        self._patient_id = value

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    @Decorator.decorator_patient_name
    def name(self, value):
        self._name = value.capitalize()

    @property
    def date(self):
        return self._date

    @date.setter
    @Decorator.decorator_date
    def date(self, value):
        self._date = value

    @property
    def time(self):
        return self._time

    @time.setter
    @Decorator.decorator_time
    def time(self, value):
        self._time = value

    @property
    def duration_in_minutes(self):
        return self._duration_in_minutes

    @duration_in_minutes.setter
    @Decorator.decorator_time_in_minute
    def duration_in_minutes(self, value):
        self._duration_in_minutes = value

    @property
    def doctor_name(self):
        return self._doctor_name.capitalize()

    @doctor_name.setter
    @Decorator.decorator_doctor_name
    def doctor_name(self, value):
        self._doctor_name = value.capitalize()

    @property
    def department(self):
        return self._department.capitalize()

    @department.setter
    @Decorator.decorator_department
    def department(self, value):
        self._department = value.capitalize()

    def __get_dictionary(self):
        return dict((prop, getattr(self, prop)) for prop in dir(self) if not prop.startswith('__')
                    and not prop.startswith('_') and prop != "input_patient" and prop != "dictionary_for_save" and prop != "str_for_search")

    def dictionary_for_save(self):
        return dict((prop[0:], getattr(self, prop)) for prop in dir(self) if not prop.startswith('__')
                    and not prop.startswith('_') and prop != "input_patient" and prop != "dictionary_for_save" and prop != "str_for_search")

    @staticmethod
    def input_patient(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d

    def __str__(self):
        return "Patient:\n" + '\n'.join("%s : %r" % (key2, str(val2)) for (key2, val2)
                                        in self.__get_dictionary().items()) + "\n"

    def str_for_search(self):
        search_str = "\n" + '\n'.join("%s " % val2 for (key2, val2) in self.__get_dictionary().items()) + "\n"
        return str(search_str)