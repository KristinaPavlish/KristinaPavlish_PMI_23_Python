from PatientList import PatientList
from Patient import Patient
from PatientService import PatientService
from Decorator import Decorator
from Validate import Validate

def menu(patient_list):
    while 1 == 1:
        print("MENU:")
        print("************************************")
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
            file_name = Validate.validate_file_name(name)
            PatientList.save(patient_list, file_name)
            print(patient_list)
        if number == str(3):
            path = input("Enter path: ")
            path = Validate.validate_file_name(path)
            name_list = input("Input name list: ")
            patient_list.read_json_file(path, name_list)
        if number == str(4):
            for i in range(0, len(patient_list)):
                print(patient_list[i])
        if number == str(5):
            id = input("Enter id to delete: ")
            id = Decorator.enter_natural(id)
            patient_list.remove_patient_from_list(id)
            for i in range(0, len(patient_list)):
                print(patient_list[i])
        if number == str(6):
            id = input("Enter id to edit: ")
            id = Decorator.enter_natural(id)
            patient_list.edit_patient_in_list(id)
        if number == str(7):
            path_to_upload = input("Enter path to upload: ")
            path_to_upload = Validate.validate_file_name(path_to_upload)
            name_list = input("Enter name of patient list: ")
            path_to_save = input("Enter path to save: ")
            path_to_save = Validate.validate_file_name(path_to_save)
            id = input("Enter id to delete: ")
            id = Decorator.enter_natural(id)
            patient_list.remove_patient_from_file(id, path_to_upload, path_to_save, name_list)
            for i in range(0, len(patient_list)):
                print(patient_list[i])
        if number == str(8):
            path = input("Enter path to upload: ")
            path = Validate.validate_file_name(path)
            name_list = input("Enter name of patient list: ")
            id = input("Enter id to edit: ")
            id = Decorator.enter_natural(id)
            patient_list.edit_patient_in_file(id, path, name_list)
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