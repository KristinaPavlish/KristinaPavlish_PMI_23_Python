from operator import attrgetter
from Patient import Patient
import json
from Validate import Validate
import copy


class PatientList:
    def __init__(self, *patient_list):
        self.patient_list = list(patient_list[:])

    def __str__(self):
        return [str(el) for el in self.patient_list]

    def __len__(self):
        return len(self.patient_list)

    def __getitem__(self, index):
        return self.patient_list[index]

    def __setitem__(self, key, value):
        self.patient_list[key] = value

    def append(self, patient):
        self.patient_list.append(patient)

    def remove_patient_from_list(self, other_id):
        element = None
        for x in self.patient_list:
            if int(x.patient_id) == int(other_id):
                element = x
                break
        if element is not None:
            self.patient_list.remove(element)

    def remove_patient_from_file(self, other_id, path_to_save):
        PatientList.read_file(self, "patient_id", "name", "date", "time", "duration_in_minutes",
                              "doctor_name", "department")
        PatientList.remove_patient_from_list(self, other_id)
        PatientList.save(self, path_to_save)

    def edit_patient_in_list(self, other_id):
        args = "_name", "_date", "_time", "_duration_in_minutes", "_doctor_name", "_department"
        element_id = 0
        for x in self.patient_list:
            if int(x.patient_id) == int(other_id):
                copy_x = copy.copy(x)
                print("\nPatient to edit: ")
                print(x)
                print("\nProperty to edit: ")
                for prop in args:
                    print(prop)
                property_to_edit = input("Enter property to edit: ")
                setattr(x, property_to_edit, input("Enter " + str(property_to_edit) + ": "))
                try:
                    dictionary = x.dictionary_for_save()
                    print(str(dictionary))
                    patient = Patient(**dictionary)
                    x = patient
                except Exception as e:
                    print(e)
                    PatientList.remove_patient_from_list(self, other_id)
                    continue
                x.patient_id = int(other_id)
                break
            element_id += 1

    def edit_patient_in_file(self, other_id, path_to_save):
        PatientList.read_file(self, "patient_id", "name", "date", "time", "duration_in_minutes", "doctor_name",
                              "department")
        PatientList.edit_patient_in_list(self, other_id)
        PatientList.save(self, path_to_save)

    def search(self, element_to_find):
        finded_patient = PatientList()
        for patient in self.patient_list:
            str_patient = str(patient.str_for_search())
            if str(element_to_find) in str_patient:
                print(patient)
                finded_patient.append(patient)
        return finded_patient

    def sort(self):
        property = input("Enter property to sort: ")
        self.patient_list = sorted(self.patient_list, key=attrgetter(property))
        return PatientList(sorted(self.patient_list, key=attrgetter(property)))

    def save(self, path=None):
        dt = {}
        dt.update(vars(self))
        with open(path, "w", encoding='utf-8') as file:
            json.dump([elem.dictionary_for_save() for elem in self.patient_list], file, cls=PatientEncoder)
        file.close()

    @staticmethod
    def read_json_file():
        name = input("Enter file name (to read): ")
        file_name = Validate.validate_file_name(name)
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            for i, product in enumerate(data):
                yield product
        json_file.close()

    def read_file(self, *args):
        list_uploaded_patient = PatientList.read_json_file()
        lst = []
        patient_for_check = Patient()
        counter = 0
        for elem in list_uploaded_patient:
            patient = elem
            counter += 1
            for prop in args:
                try:
                    setattr(patient_for_check, prop, elem[prop])
                except Exception as err:
                    lst.append("Patient " + str(counter))
                    lst.append(err)
                    patient = None
                    print(str(prop) + " incorrect")
                    break
            if patient is not None:
                self.patient_list.append(Patient(**elem))
        for error in lst:
            print(error)


class PatientEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
