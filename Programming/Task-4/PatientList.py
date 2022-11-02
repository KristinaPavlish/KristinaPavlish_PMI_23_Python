from operator import attrgetter
from Patient import Patient
import json
from Decorator import Decorator
from Validate import Validate
from Error import PatientIdIncorrect, NameIncorrect, DateIncorrect, TimeIncorrect, DurationInMinuteIncorrect, \
    DepartmentIncorrect, DoctorNameIncorrect


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
        with open(path, "w", encoding='utf-8') as file:
            json.dump([ob.__dict__ for ob in self.patient_list], file, cls=PatientEncoder)
        file.close()

    def read_json_file(self):
        # file_name = input("Enter path: ")
        # file_name = Validate.validate_file_name(file_name)
        with open("test.json", 'r') as json_file:
            data = json.load(json_file)
            for i, elem in enumerate(data):
                try:
                    self.patient_list.append(Patient(**elem))
                except Exception as e:
                    print("Patient" + str(i + 1) + ": " + str(e))
                    continue
        json_file.close()


class PatientEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
