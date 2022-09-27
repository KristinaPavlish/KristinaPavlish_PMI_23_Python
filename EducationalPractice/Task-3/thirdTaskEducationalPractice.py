from LinkedList import LinkedList
from Validator import Validator


def menu(linked_list):
    while 1 == 1:
        print("MENU:")
        print("[1] - Enter size")
        print("[2] - Go to additional menu")
        print("[2] - Exit")
        number = input("Enter option : ")
        if number == str(1):
            linked_list.enter_size()
            additional_menu(linked_list)
        if number == str(2):
            additional_menu(linked_list)
        if number == str(3):
            break


def additional_menu(linked_list):
    while 1 == 1:
        print("Additional menu:")
        print("[1] - Generate list")
        print("[2] - Enter list")
        print("[3] - Show list")
        print("[4] - Delete list")
        print("[5] - Operations")
        print("[6] - Go to main menu")
        print("[7] - Exit")
        number = input("Enter option : ")
        if number == str(1):
            linked_list.generate_array()
        if number == str(2):
            linked_list.entering_list()
        if number == str(3):
            print(linked_list)
        if number == str(4):
            linked_list.delete_all_list()
        if number == str(5):
            operations(linked_list)
        if number == str(6):
            menu(linked_list)
        if number == str(7):
            break


def operations(linked_list):
    while 1 == 1:
        print("Operations:")
        print("[1] - Add element")
        print("[2] - Delete element")
        print("[3] - Compress list")
        print("[4] - Go to additional menu")
        print("[5] - Exit")
        number = input("Enter option : ")
        if number == str(1):
            index = input("Enter index to add: ")
            is_index_correct = Validator.is_natural(index)
            while not is_index_correct:
                index = input("Enter correct index to add: ")
                is_index_correct = Validator.is_natural(index)
            index = int(index)

            element = input("Enter element: ")
            is_element_correct = Validator.is_natural(index)
            while not is_element_correct:
                element = input("Enter correct element to add: ")
                is_element_correct = Validator.is_natural(index)
            linked_list.add_str_element_in_position(element, index, False)

        if number == str(2):
            index = input("Enter index to delete: ")
            is_index_correct = Validator.is_natural(index)
            while not is_index_correct:
                index = input("Enter correct index to delete: ")
                is_index_correct = Validator.is_natural(index)
            index = int(index)
            linked_list.delete_str_element_by_position(index)

        if number == str(3):
            linked_list.compress_the_array()
            print(linked_list)
        if number == str(4):
            additional_menu(linked_list)
        if number == str(5):
            break


if __name__ == '__main__':
    linked_list = LinkedList()
    menu(linked_list)
