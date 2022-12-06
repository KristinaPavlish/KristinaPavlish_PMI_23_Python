import json

from Validator import Validator
from Patient import Patient
from Error import PatientIdIncorrect, NameIncorrect, DateIncorrect, TimeIncorrect, DurationInMinuteIncorrect, \
    DoctorNameIncorrect, DepartmentIncorrect


class PatientService(Patient):

    @staticmethod
    def input_patient_from_keyboard(patient):
        patient.patient_id = input("Input Patient Id: ")
        is_patient_id_correct = Validator.is_natural(patient.patient_id)
        while not is_patient_id_correct:
            patient.patient_id = input("Input Patient Id: ")
            is_patient_id_correct = Validator.is_natural(patient.patient_id)
        patient.patient_id = int(patient.patient_id)

        patient.name = input("Input Patient Name: ")
        is_name_correct = Validator.is_only_letter(patient.name)
        while not is_name_correct:
            patient.name = input("Input Patient Name: ")
            is_name_correct = Validator.is_only_letter(patient.name)

        patient.date = input("Input Patient Date: ")
        is_date_correct = Validator.is_date_correct(patient.date)
        while not is_date_correct:
            patient.date = input("Input Patient Date: ")
            is_date_correct = Validator.is_date_correct(patient.date)

        patient.time = input("Input Patient Time: ")
        is_time_correct = Validator.is_time_correct(patient.time)
        while not is_time_correct:
            patient.time = input("Input Patient Time: ")
            is_time_correct = Validator.is_time_correct(patient.time)

        patient.duration_in_minutes = input("Input Patient Time in Minute: ")
        is_duration_in_minutes_correct = Validator.is_natural(patient.duration_in_minutes)
        while not is_duration_in_minutes_correct:
            patient.duration_in_minutes = input("Input Patient Time in Minute: ")
            is_duration_in_minutes_correct = Validator.is_natural(patient.duration_in_minutes)
        patient.duration_in_minutes = int(patient.duration_in_minutes)

        patient.doctor_name = input("Input Doctor Name: ")
        is_doctor_name_correct = Validator.is_only_letter(patient.doctor_name)
        while not is_doctor_name_correct:
            patient.doctor_name = input("Input Doctor Name: ")
            is_doctor_name_correct = Validator.is_only_letter(patient.doctor_name)

        patient.department = input("Input Department: ")
        is_department_correct = Validator.is_only_letter(patient.department)
        while not is_department_correct:
            patient.department = input("Input Department: ")
            is_department_correct = Validator.is_only_letter(patient.department)
        return patient

    @staticmethod
    def isValid(patient):
        if not Validator.is_natural(patient.patient_id):
            raise PatientIdIncorrect()

        if not Validator.is_only_letter(patient.name):
            raise NameIncorrect()

        if not Validator.is_date_correct(patient.date):
            raise DateIncorrect()

        if not Validator.is_time_correct(patient.time):
            raise TimeIncorrect()

        if not Validator.is_natural(patient.duration_in_minutes):
            raise DurationInMinuteIncorrect()

        if not Validator.is_only_letter(patient.doctor_name):
            raise DoctorNameIncorrect()

        if not Validator.is_only_letter(patient.department):
            raise DepartmentIncorrect()


    @staticmethod
    def valid_patient(patient):
        is_patient_id_correct = Validator.is_natural(patient.patient_id)
        while not is_patient_id_correct:
            patient.patient_id = input("Input Patient Id: ")
            is_patient_id_correct = Validator.is_natural(patient.patient_id)
        patient.patient_id = int(patient.patient_id)

        is_name_correct = Validator.is_only_letter(patient.name)
        while not is_name_correct:
            patient.name = input("Input Patient Name: ")
            is_name_correct = Validator.is_only_letter(patient.name)

        is_date_correct = Validator.is_date_correct(patient.date)
        while not is_date_correct:
            patient.date = input("Input Patient Date: ")
            is_date_correct = Validator.is_date_correct(patient.date)

        is_time_correct = Validator.is_time_correct(patient.time)
        while not is_time_correct:
            patient.time = input("Input Patient Time: ")
            is_time_correct = Validator.is_time_correct(patient.time)

        is_duration_in_minutes_correct = Validator.is_natural(patient.duration_in_minutes)
        while not is_duration_in_minutes_correct:
            patient.duration_in_minutes = input("Input Patient Time in Minute: ")
            is_duration_in_minutes_correct = Validator.is_natural(patient.duration_in_minutes)
        patient.duration_in_minutes = int(patient.duration_in_minutes)

        is_doctor_name_correct = Validator.is_only_letter(patient.doctor_name)
        while not is_doctor_name_correct:
            patient.doctor_name = input("Input Doctor Name: ")
            is_doctor_name_correct = Validator.is_only_letter(patient.doctor_name)

        is_department_correct = Validator.is_only_letter(patient.department)
        while not is_department_correct:
            patient.department = input("Input Department: ")
            is_department_correct = Validator.is_only_letter(patient.department)
        return patient
