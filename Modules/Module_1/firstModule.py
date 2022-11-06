from BookingList import BookingList
from Booking import Booking
def menu(patient_list):
    while 1 == 1:
        print("MENU:")
        print("\n************************************")
        print("[1] - Add booking + ")

        print("[2] - Exit")
        print("************************************\n")

        number = input("Enter option : ")
        if number == str(1):
            booking = Booking(None, None, None, None)
            booking.input_booking()
            print(booking)
        if number == str(2):
            break


if __name__ == '__main__':
    booking_list = BookingList()
    menu(booking_list)