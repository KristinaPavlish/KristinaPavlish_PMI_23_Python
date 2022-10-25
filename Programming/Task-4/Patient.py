from Decorator import Decorator


class Patient(object):
    def __init__(self, **kwargs):
        for (name_prop, value) in kwargs.items():
            print(name_prop+" "+value)
            setattr(self, name_prop, kwargs.get(name_prop, value))

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
        self._name = value

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
        self._doctor_name = value

    @property
    def department(self):
        return self._department

    @department.setter
    @Decorator.decorator_department
    def department(self, value):
        self._department = value

    def _to_dict(self):
        return dict(self._patient_id + self._name + self._date + self._time + self._doctor_name + self._department)
    #def _to_dict(self):
    #    return dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')
    #                 and name != "input_patient" and name != "_str_for_search" and name != "_dict_to_obj" and name != "_to_dict" and name != "_Patient__to_dict")

   # def ___to_dict(self):
   #     return dict((name, getattr(self, name[1:len(name)])) for name in dir(self)
   #                 if not name.startswith(
   #         '__')  and name != "input_patient" and name != "to_patient" and name != "str_for_search" and
   #                 name != "dict_to_obj" and name != "_to_dict" and name != "_Patient__to_obj" and name != "Patient___to_patient" and name != "Patient___to_dict")

    @staticmethod
    def input_patient(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d

    def __str__(self):
        return "---Patient---\n"\
               + "\nId:" + str(self.patient_id) \
               + "\nName:" + str(self.name) \
               + "\nDate:" + str(self.date)\
               + "\nTime: " + str(self.time) \
               + "\nDoctor name: " + str(self.doctor_name)\
               + "\nDepartment: " + str(self.department)

    def _str_for_search(self):
        return "\n" + '\n'.join("%s " % val2 for (key2, val2)
                                in self._to_dict().items()) + "\n"
