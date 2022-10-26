from LinkedList import LinkedList
from Validator import Validator
from Strategy import Strategy, StrategyGenerateWithGenerator, StrategyGenerateWithReadFromFile


def menu(linked_list, strategy):
    while 1 == 1:
        print("Additional menu:")
        print("[0] - Choose generate using generator strategy")
        print("[1] - Choose generate list with reading from file")
        print("[2] - Generate list")
        print("[3] - Delete element")
        print("[4] - Delete element by two position")
        print("[5] - Compress array")
        print("[6] - Show array")
        print("[7] - Exit")
        number = input("Enter option : ")
        if number == str(0):
            strategy = StrategyGenerateWithGenerator(Strategy)
        if number == str(1):
            strategy = StrategyGenerateWithReadFromFile(Strategy)
        if number == str(2):
            list_to_add = strategy.generate_list()
            list_to_add = strategy.get_list()
            index = input("Enter index to add elements: ")
            is_index_correct = Validator.is_natural(index)
            while not is_index_correct:
                index = input("Enter correct index to add elements: ")
                is_index_correct = Validator.is_natural(index)
            index = int(index)
            linked_list = linked_list.add_elements_by_position(list_to_add, index)
        if number == str(3):
            index = input("Enter index to delete: ")
            is_index_correct = Validator.is_natural(index)
            while not is_index_correct:
                index = input("Enter correct index to delete: ")
                is_index_correct = Validator.is_natural(index)
            index = int(index)
            linked_list.delete_str_element_by_position(index)

        if number == str(4):
            first_position = input("Enter first position: ")
            is_index_correct = Validator.is_natural(first_position)
            while not is_index_correct:
                first_position = input("Enter correct index to add: ")
                is_index_correct = Validator.is_natural(first_position)
            first_position = int(first_position)

            second_position = input("Enter second position: ")
            is_index_correct = Validator.is_natural(second_position)
            while not is_index_correct:
                second_position = input("Enter correct index to add: ")
                is_index_correct = Validator.is_natural(second_position)
            second_position = int(second_position)
            linked_list.delete_str_element_by_two_position(first_position, second_position)
        if number == str(5):
            linked_list.compress_the_array()
            print(linked_list)
        if number == str(6):
            print(linked_list)
        if number == str(7):
            break


if __name__ == '__main__':
    linked_list = LinkedList()
    strategy = Strategy()
    menu(linked_list, strategy)
