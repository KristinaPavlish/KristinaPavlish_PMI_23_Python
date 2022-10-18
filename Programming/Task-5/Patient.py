from Decorator import Decorator


class Patient:

    def __init__(self, patient_id=None, name=None, date=None, time=None, duration_in_minutes=None, doctor_name=None,
                 department=None):
        self.patient_id = patient_id
        self.name = name
        self.date = date
        self.time = time
        self.duration_in_minutes = duration_in_minutes
        self.doctor_name = doctor_name
        self.department = department

    def __str__(self):
        return "Patient Id: {0}, Name: {1}, Date: {2}, Time: {3}, Duration: {4} (in minutes), Doctor Name: {5}, Department: {6}" \
            .format(
            self.patient_id,
            self.name,
            self.date,
            self.time,
            self.duration_in_minutes,
            self.doctor_name,
            self.department
        )

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

    @Decorator.decorator_natural
    def patient_id(self, value):
        self.patient_id = value

    @Decorator.decorator_word
    def name(self, value):
        self.name = value

    @Decorator.decorator_date
    def date(self, value):
        self.date = value

    @Decorator.decorator_time
    def time(self, value):
        self.time = value

    @Decorator.decorator_natural
    def duration_in_minutes(self, value):
        self.duration_in_minutes = value

    @Decorator.decorator_word
    def doctor_name(self, value):
        self.doctor_name = value

    @Decorator.decorator_word
    def department(self, value):
        self.department = value
