import json

from Decorator import Decorator
from Validate import Validate
from Patient import Patient
from Error import PatientIdIncorrect, NameIncorrect, DateIncorrect, TimeIncorrect, DurationInMinuteIncorrect, \
    DoctorNameIncorrect, DepartmentIncorrect


class PatientService(Patient):

    @staticmethod
    def input_patient_from_keyboard(patient):
        patient.patient_id = input("Input Patient Id: ")
        patient.patient_id = Decorator.enter_natural(patient.patient_id)

        patient.name = input("Input Patient Name: ")
        patient.name = Decorator.enter_words(patient.name)

        patient.date = input("Input Patient Date: ")
        patient.date = Decorator.enter_date(patient.date)

        patient.time = input("Input Patient Time: ")
        patient.time = Decorator.enter_time(patient.time)

        patient.duration_in_minutes = input("Input Patient Time in Minute: ")
        patient.duration_in_minutes = Decorator.enter_natural(patient.duration_in_minutes)

        patient.doctor_name = input("Input Doctor Name: ")
        patient.doctor_name = Decorator.enter_words(patient.doctor_name)

        patient.department = input("Input Department: ")
        patient.department = Decorator.enter_words(patient.department)
        return patient

    @staticmethod
    def valid_patient(patient):
        patient.patient_id = Decorator.enter_date(patient.patient_id)

        patient.name = Decorator.enter_words(patient.name)

        patient.date = Decorator.enter_date(patient.date)

        patient.time = Decorator.enter_time(patient.time)

        patient.duration_in_minutes = Decorator.enter_natural(patient.duration_in_minutes)

        patient.doctor_name = Decorator.enter_words(patient.doctor_name)

        patient.department = Decorator.enter_words(patient.department)
        return patient