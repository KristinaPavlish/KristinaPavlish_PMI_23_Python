from PatientList import PatientList
from Patient import Patient
from Decorator import Decorator
from Validate import Validate


def menu(patient_list):
    while 1 == 1:
        print("MENU:")
        print("************************************")
        print("[1] - Add patient")
        print("[2] - Save list")
        print("[3] - Upload list")
        print("[4] - Show list")
        print("[5] - Delete patient from list")
        print("[6] - Edit patient in list")
        print("[7] - Delete patient from file")
        print("[8] - Edit patient in file")
        print("[9] - Sort list")
        print("[10] - Search patient")
        print("[11] - Exit")
        print("************************************\n")

        number = input("Enter option : ")
        if number == str(1):
            add_patient_to_list(patient_list)
        if number == str(2):
            save_list(patient_list)
        if number == str(3):
            upload_list(patient_list)
        if number == str(4):
            for patient in patient_list:
                print(patient)
        if number == str(5):
            delete_patient_by_id(patient_list)
        if number == str(6):
            edit_patient_by_id(patient_list)
        if number == str(7):
            delete_patient_from_file(patient_list)
        if number == str(8):
            edit_in_file(patient_list)
        if number == str(9):
            sort_list(patient_list)
        if number == str(10):
            search_in_list(patient_list)
        if number == str(11):
            break


@Decorator.validate_inp
def add_patient_to_list(list_of_patient):
    patient = Patient.input_patient("patient_id", "name", "date", "time", "duration_in_minutes", "doctor_name",
                                    "department")

    list_of_patient.append(Patient(**patient))


@Decorator.validate_inp
def save_list(list_of_patient):
    name = input("Enter path: ")
    show_list(list_of_patient)
    file_name = Validate.validate_file_name(name)
    list_of_patient.save(file_name)


def upload_list(list_of_patient):
    PatientList.read_file(list_of_patient, "patient_id", "name", "date", "time", "duration_in_minutes", "doctor_name",
                          "department")


@Decorator.validate_inp
def delete_patient_by_id(list_of_patient):
    id = input("Enter id to delete: ")
    id_to_del = is_id_correct(id)
    list_of_patient.remove_patient_from_list(id_to_del)


def is_id_correct(id):
    is_natural = Validate.is_natural_elem(id)
    while not is_natural:
        id = input("Enter id to delete: ")
        is_natural = Validate.is_natural_elem(id)
    return id


@Decorator.validate_inp
def edit_patient_by_id(list_of_patient):
    id = input("Enter id to edit: ")
    id_to_edit = is_id_correct(id)
    list_of_patient.edit_patient_in_list(id_to_edit)


@Decorator.validate_inp
def delete_patient_from_file(list_of_patient):
    id = input("Enter id to delete: ")
    id_to_del = is_id_correct(id)
    path_to_save = input("Enter path to save: ")
    path_to_save = Validate.validate_file_name(path_to_save)
    list_of_patient.remove_patient_from_file(id_to_del, path_to_save)


@Decorator.validate_inp
def edit_in_file(list_of_patient):
    id = input("Enter id to edit: ")
    id_to_edit = is_id_correct(id)
    path_to_save = input("Enter path to save: ")
    path_to_save = Validate.validate_file_name(path_to_save)
    list_of_patient.edit_patient_in_file(id_to_edit, path_to_save)


@Decorator.validate_inp
def sort_list(list_of_patient):
    print("Fields to sort: <patient_id> <name> <date> <time> <duration_in_minutes> <doctor_name> <department>")
    list_of_patient.sort()


def show_list(list_of_patient):
    print(len(list_of_patient))
    for patient in list_of_patient:
        print(patient)


def search_in_list(list_of_patient):
    element_to_search = input("Enter element to search: ")
    PatientList(list_of_patient.search(element_to_search))


if __name__ == '__main__':
    patient_list = PatientList()
    menu(patient_list)
