from PatientList import PatientList
from Patient import Patient
from PatientService import PatientService
from Validator import Validator


def menu(patient_list):
    while 1 == 1:
        print("MENU:")
        print("\n************************************")
        print("[1] - Add patient + ")
        print("[2] - Save list + ")
        print("[3] - Upload list+")
        print("[4] - Show list+")
        print("[5] - Delete patient from list+")
        print("[6] - Edit patient in list+")
        print("[7] - Delete patient from file+")
        print("[8] - Edit patient in file+")
        print("[9] - Sort list")
        print("[10] - Search patient")
        print("[11] - Exit")
        print("************************************\n")

        number = input("Enter option : ")
        if number == str(1):
            patient = Patient()
            patient1 = PatientService.input_patient_from_keyboard(patient)
            print(patient1)
            PatientList.add_patient(patient_list, patient1)
        if number == str(2):
            name = input("Enter path: ")
            file_name = Validator.validate_file_name(name)
            PatientList.save(patient_list, file_name)
            print(patient_list)
        if number == str(3):
            name = input("Enter path: ")
            file_name = Validator.validate_file_name(name)
            name_list = input("Enter name of patient list: ")
            PatientList.upload(patient_list, file_name, name_list)
        if number == str(4):
            for i in range(0, len(patient_list)):
                print(patient_list[i])
        if number == str(5):
            id = input("Enter id to delete: ")
            is_patient_id_correct = Validator.is_natural(id)
            while not is_patient_id_correct:
                id = input("Input Patient Id: ")
                is_patient_id_correct = Validator.is_natural(id)
            patient_list.remove_patient_from_list(id)
            for i in range(0, len(patient_list)):
                print(patient_list[i])
        if number == str(6):
            id = input("Enter id to edit: ")
            patient_list.edit_patient_in_list(id)
        if number == str(7):
            id = input("Enter id to delete: ")
            is_patient_id_correct = Validator.is_natural(id)
            while not is_patient_id_correct:
                id = input("Input Patient Id: ")
                is_patient_id_correct = Validator.is_natural(id)
            patient_list.remove_patient_from_file(id)
            for i in range(0, len(patient_list)):
                print(patient_list[i])
        if number == str(8):
            id = input("Enter id to edit: ")
            patient_list.edit_patient_in_file(id)
        if number == str(9):
            print("Fields to sort: <patient_id> <name> <date> <time> <duration_in_minutes> <doctor_name> <department>")
            patient_list.sort()
            for i in range(0, len(patient_list)):
                print(patient_list[i])
        if number == str(10):
            element_to_search = input("Enter element to search: ")
            print(patient_list.search(element_to_search))
        if number == str(11):
            break


if __name__ == '__main__':
    patient_list = PatientList()
    menu(patient_list)
