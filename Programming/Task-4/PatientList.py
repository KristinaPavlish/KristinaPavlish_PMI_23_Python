import uuid
from operator import attrgetter
from Patient import Patient
import json
from Decorator import Decorator
from Validate import Validate


class PatientList:
    def __init__(self, *patient_list):
        self.patient_list = list(patient_list[:])

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
        self.patient_list.append(patient)

    def remove_patient_from_list(self, other_id):
        element = None
        for x in self.patient_list:
            if str(x.patient_id) == other_id:
                element = x
                break
        if element is not None:
            self.patient_list.remove(element)

    @Decorator.validateFileName()
    def remove_patient_from_file(self, other_id, path_to_upload, path_to_save, name_list):
        PatientList.read_json_file(self, path_to_upload, name_list)
        PatientList.remove_patient_from_list(self, other_id)
        PatientList.save(self, path_to_save)

    def edit_patient_in_list(self, other_id):
        element_id = 0
        for x in self.patient_list:
            if str(x.patient_id) == other_id:
                print("Patient to edit: ")
                print(x)
                x = Patient.input_patient("patient_id", "name", "date", "time", "duration_in_minutes", "doctor_name",
                                          "department")
                x.patient_id = int(other_id)
                break
            element_id += 1

    @Decorator.validateFileName()
    def edit_patient_in_file(self, other_id, path, name_list):
        PatientList.read_json_file(self, path, name_list)
        PatientList.edit_patient_in_list(self, other_id)

    def search(self, element_to_find):
        finded_elements = []
        for i in range(0, len(self.patient_list)):
            str_patient = self.patient_list[i]._str_for_search()
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
        print(type(dt))
        with open(path, "w") as file:
            json.dump(dt, file, cls=PatientEncoder)
        file.close()

    @Decorator.validate_inp
    def read_json_file(self):
        file_name = input("Enter path: ")
        file_name = Validate.validate_file_name(file_name)
        name_list = input("Input name list: ")
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            for i, element in enumerate(data[name_list]):
                patient = Patient()
                Patient._dict_to_obj(patient, element)
                self.add_patient(patient)
        json_file.close()
        return data, name_list

    @Decorator.validate_inp
    def save_upload_to_list(self):
        patient = Patient()
        data, name_list = self.read_json_file()
        for i, element in enumerate(data[name_list]):
            try:
                patient_to_add = patient._to_patient(element)
                print(patient_to_add.name)
                print(type(patient_to_add))
                self.add_patient(patient_to_add)
            except ValueError as e:
                print("Line" + str(i * (len(element) + 1) + 3) + ": " + str(e))
                continue


class PatientEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
