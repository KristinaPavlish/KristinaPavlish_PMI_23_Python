class Memento:
    def __int__(self, patient_list_, message_):
        self.patient_list = patient_list_
        self.message = message_

    def __str__(self):
        return [str(el) for el in self.patient_list]

    def get_list(self):
        return self.patient_list

    def set_message(self, mess):
        self.message = mess

    def get_message(self):
        return self.message
