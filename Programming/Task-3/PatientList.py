from operator import attrgetter
from Patient import Patient
import json
from PatientService import PatientService
from Validator import Validator


class PatientList:
    def __init__(self, patient_list=None):
        self.patient_list = []
        if patient_list is not None:
            self.patient_list = patient_list

    def __str__(self):
        output = ""
        for i in range(0, len(self.patient_list)):
            output += str(self.patient_list[i])
            output += "\n"
        return output

    def __len__(self):
        return len(self.patient_list)

    def __getitem__(self, index):
        return self.patient_list[index]

    def __setitem__(self, key, value):
        self.patient_list[key] = value

    def add_patient(self, patient):
        if not PatientService.isValid(patient):
            self.patient_list.append(patient)

    def remove_patient_from_list(self, other_id):
        element = None
        for x in self.patient_list:
            if str(x.patient_id) == other_id:
                element = x
                break
        if element is not None:
            self.patient_list.remove(element)

    def remove_patient_from_file(self, other_id):
        name = input("Enter path to upload: ")
        file_name = Validator.validate_file_name(name)
        name_list = input("Enter name of patient list: ")
        PatientList.upload(self, file_name, name_list)
        PatientList.remove_patient_from_list(self, other_id)
        name = input("Enter path to save: ")
        file_name = Validator.validate_file_name(name)
        PatientList.save(self, file_name)

    def edit_patient_in_list(self, other_id):
        element_id = 0
        for x in self.patient_list:
            if str(x.patient_id) == other_id:
                print("Patient to edit: ")
                print(x)
                x = PatientService.input_patient_from_keyboard(x)
                x.patient_id = int(other_id)
                break
            element_id += 1

    def edit_patient_in_file(self, other_id):
        name = input("Enter path to upload: ")
        file_name = Validator.validate_file_name(name)
        name_list = input("Enter name of patient list: ")
        PatientList.upload(self, file_name, name_list)
        PatientList.edit_patient_in_list(self, other_id)

    def search(self, element_to_find):
        finded_elements = []
        for i in range(0, len(self.patient_list)):
            str_patient = self.patient_list[i].str_for_search()
            if element_to_find in str_patient:
                finded_elements.append(self.patient_list[i])
        return PatientList(finded_elements)

    def sort(self):
        property = input("Enter property to sort: ")
        self.patient_list = sorted(self.patient_list, key=attrgetter(property))
        return PatientList(sorted(self.patient_list, key=attrgetter(property)))

    def save(self, path=None):
        dt = {}
        dt.update(vars(self))

        with open(path, "w") as file:
            json.dump(dt, file, cls=PatientEncoder)

    def upload(self, file_name, name_list):
        with open(file_name) as json_file:
            data = json.load(json_file)
            for i in data[name_list]:
                patient = Patient()
                patient.patient_id = i['patient_id']
                patient.name = i['name']
                patient.date = i['date']
                patient.time = i['time']
                patient.duration_in_minutes = i['duration_in_minutes']
                patient.doctor_name = i['doctor_name']
                patient.department = i['department']
                patient = PatientService.valid_patient(patient)
                PatientList.add_patient(self, patient)


class PatientEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
