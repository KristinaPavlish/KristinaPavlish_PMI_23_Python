from operator import attrgetter
from Patient import Patient
import json
from PatientService import PatientService
from Decorator import Decorator
from Memento import Memento


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
                x = PatientService.input_patient_from_keyboard(x)
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

    def read_json_file(self, file_name, name_list):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            for i, element in enumerate(data[name_list]):
                elem = Patient(**element)
                self.add_patient(elem)
        json_file.close()

    def save_memento(self, message):
        copy_list = self.patient_list.copy()
        print(message)
        return copy_list

    def restore_memento(self, memento: Memento):
        self.patient_list = memento.get_list()
        print(f"Patient list has changed to:")
        for i in range(0, len(self.patient_list)):
            print(self.patient_list[i])


class PatientEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
