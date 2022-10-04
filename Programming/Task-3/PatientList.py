from operator import attrgetter
from Patient import Patient
import json


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

    def add_patient(self, other: Patient):
        path = input("Enter name file: ")
        if other.isValid():
            self.patient_list.append(other)
            self.save(path)
            self.upload(path)

    def remove_patient(self, other_id):
        path = input("Enter name file: ")
        element = None
        for x in self.patient_list:
            if x.patient_id == other_id:
                element = x
                break
        if element is not None:
            self.patient_list.remove(element)
        self.save(path)

    def edit_patient(self, other_id, other: Patient):
        other.isValid()
        path = input("Enter name file: ")
        element = None
        element_id = 0
        for x in self.patient_list:
            if x.patient_id == other_id:
                element = x
                break
            element_id += 1
        other.patient_id = other_id
        if element is not None:
            self.patient_list[element_id] = other
        self.save(path)

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

    def upload(self, path=None):
        def read_json(_path):
            with open(_path, "r") as file:
                return json.load(file)

        data = read_json(path)
        return PatientList(**data)


class PatientEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
