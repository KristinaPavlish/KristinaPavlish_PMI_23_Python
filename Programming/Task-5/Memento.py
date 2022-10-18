class Memento:
    def __int__(self, patient_list_, message_):
        self.patient_list = patient_list_
        self.message = message_

    def get_list(self):
        return self.patient_list

    def get_message(self):
        return self.message
