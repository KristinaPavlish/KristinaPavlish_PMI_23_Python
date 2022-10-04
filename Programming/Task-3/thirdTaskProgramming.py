import operator

from Validator import Validator
from PatientList import PatientList
from Patient import Patient


def menu(patient_list):
    while 1 == 1:
        print("MENU:")
        print("[1] - Enter patient")
        print("[2] - Sort list")
        print("[3] - Search patient")
        print("[4] - Edit patient")
        print("[5] - Delete patient")
        print("[6] - Show list")
        print("[7] - Exit")
        number = input("Enter option : ")
        if number == str(1):
            input_patient = input_patient_from_keyboard(Patient())
            print(input_patient)
            patient_list.add_patient(input_patient)
            print(patient_list)
        if number == str(2):
            patient_list.sort()
            print(patient_list)
        if number == str(3):
            element_to_search = input("Enter element to search: ")
            print(patient_list.search(element_to_search))
            print(patient_list)
        if number == str(4):
            patient = Patient()
            print("Enter patient to edit: ")
            input_patient = input_patient_from_keyboard(patient)
            id = input("Enter id to replace: ")
            patient_list.edit_patient(id, input_patient)
            print(patient_list)
        if number == str(5):
            id = input("Enter id to delete: ")
            patient_list.remove_patient(id)
            print(patient_list)
        if number == str(6):
            print(patient_list)
        if number == str(7):
            break


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


if __name__ == '__main__':
    patient_list = PatientList()
    menu(patient_list)
