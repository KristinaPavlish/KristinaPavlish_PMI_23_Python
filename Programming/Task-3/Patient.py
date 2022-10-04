import json

from Validator import Validator
from Error import Error, ValueIncorrect


class Patient:

    def __init__(self, patient_id=None, name=None, date=None, time=None, duration_in_minutes=None, doctor_name=None, department=None):
        self.patient_id = patient_id
        self.name = name
        self.date = date
        self.time = time
        self.duration_in_minutes = duration_in_minutes
        self.doctor_name = doctor_name
        self.department = department

    def isValid(self):
        if not Validator.is_natural(self.patient_id):
            raise ValueIncorrect()

        if not Validator.is_only_letter(self.name):
            raise ValueIncorrect()

        if not Validator.is_date_correct(self.date):
            raise ValueIncorrect()

        if not Validator.is_time_correct(self.time):
            raise ValueIncorrect()

        if not Validator.is_natural(self.duration_in_minutes):
            raise ValueIncorrect()

        if not Validator.is_only_letter(self.doctor_name):
            raise ValueIncorrect()

        if not Validator.is_only_letter(self.department):
            raise ValueIncorrect()

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