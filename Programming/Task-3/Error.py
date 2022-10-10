class Error(Exception):
    pass


class ValueIncorrect(Error):
    def __init__(self, message="Value incorrect"):
        self.message = message
        super().__init__(self.message)


class PatientIdIncorrect(Error):
    def __init__(self, message="Patient id incorrect"):
        self.message = message
        super().__init__(self.message)


class NameIncorrect(Error):
    def __init__(self, message="Name incorrect"):
        self.message = message
        super().__init__(self.message)


class DateIncorrect(Error):
    def __init__(self, message="Date incorrect"):
        self.message = message
        super().__init__(self.message)


class TimeIncorrect(Error):
    def __init__(self, message="Time incorrect"):
        self.message = message
        super().__init__(self.message)


class DurationInMinuteIncorrect(Error):
    def __init__(self, message="Duration in minutes incorrect"):
        self.message = message
        super().__init__(self.message)


class DoctorNameIncorrect(Error):
    def __init__(self, message="Doctor name incorrect"):
        self.message = message
        super().__init__(self.message)


class DepartmentIncorrect(Error):
    def __init__(self, message="Department incorrect"):
        self.message = message
        super().__init__(self.message)
