from Decorator import Decorator


class Patient:
    def __init__(self, **kwargs):
        for (property_, default) in kwargs.items():
            setattr(self, property_, kwargs.get(property_, default))

    @staticmethod
    @classmethod
    def __to_obj(**entries):
        __dict__.update(entries)
    @property
    def patient_id(self):
        return self.patient_id

    @property
    def name(self):
        return self.name

    @property
    def date(self):
        return self.date

    @property
    def time(self):
        return self.time

    @property
    def duration_in_minutes(self):
        return self.duration_in_minutes

    @property
    def doctor_name(self):
        return self.doctor_name

    @property
    def department(self):
        return self.department

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')
                    and not name.startswith('_'))

    def __str__(self):
        """
        (Product)->(str)
        returns a string representing Product.
         """
        return "Product:\n" + '\n'.join("%s : %r" % (key2, str(val2)) for (key2, val2)
                                        in self.__get_dictionary().items()) + "\n"

    def str_for_search(self):
        return "{0} {1} {2} {3} {4} {5} {6}" \
            .format(
            self.patient_id,
            self.name,
            self.date,
            self.time,
            self.duration_in_minutes,
            self.doctor_name,
            self.department
        )




    @patient_id.setter
    @Decorator.decorator_natural
    def patient_id(self, value):
        self.patient_id = value

    @name.setter
    @Decorator.decorator_word
    def name(self, value):
        self.name = value

    @date.setter
    @Decorator.decorator_date
    def date(self, value):
        self.date = value

    @time.setter
    @Decorator.decorator_time
    def time(self, value):
        self.time = value

    @duration_in_minutes.setter
    @Decorator.decorator_natural
    def duration_in_minutes(self, value):
        self.duration_in_minutes = value

    @doctor_name.setter
    @Decorator.decorator_word
    def doctor_name(self, value):
        self.doctor_name = value

    @department.setter
    @Decorator.decorator_word
    def department(self, value):
        self.department = value

