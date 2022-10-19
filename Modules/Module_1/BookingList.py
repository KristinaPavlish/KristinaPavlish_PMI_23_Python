class BookingList:
    def __init__(self, booking_list=None):
        self.booking_list = []
        if booking_list is not None:
            self.patient_list = booking_list

    def __str__(self):
        output = ""
        for i in range(0, len(self.booking_list)):
            output += str(self.booking_list[i])
            output += "\n"
        return output

    def __len__(self):
        return len(self.booking_list)

    def __getitem__(self, index):
        return self.booking_list[index]

    def __setitem__(self, key, value):
        self.booking_list[key] = value

    def add_booking(self, patient):
        self.patient_list.append(patient)
