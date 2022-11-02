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
        return self._name

    @name.setter
    @Decorator.decorator_patient_name
    def name(self, value):
        self._name = value.upper()

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
        return self._doctor_name

    @doctor_name.setter
    @Decorator.decorator_doctor_name
    def doctor_name(self, value):
        self._doctor_name = value.upper()

    @property
    def department(self):
        return self._department

    @department.setter
    @Decorator.decorator_department
    def department(self, value):
        self._department = value.upper()

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')
                    and not name.startswith('_') and name != "input_patient")

    @staticmethod
    def input_patient(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d

    def __str__(self):
        return "Patient:\n" + '\n'.join("%s : %r" % (key2, str(val2)) for (key2, val2)
                                        in self.__get_dictionary().items()) + "\n"
    def _str_for_search(self):
        return "\n" + '\n'.join("%s " % val2 for (key2, val2)
                                in self.__get_dictionary().items()) + "\n"