from Validator import Validator
from LinkedList import LinkedList
import abc


class Strategy:

    def __init__(self, generate_sequence=None):
        self.generate_sequence = generate_sequence

    def get_list(self):
        linked_list = LinkedList()
        if self.generate_sequence is not None:
            linked_list = self.generate_sequence
            print(linked_list)
        return linked_list

    @abc.abstractmethod
    def generate_list(self):
        pass


class StrategyGenerateWithGenerator(Strategy):
    def generate_list(self):
        size = input("Enter size: ")
        is_index_correct = Validator.is_natural(size)
        while not is_index_correct:
            size = input("Enter correct size: ")
            is_index_correct = Validator.is_natural(size)
        size = int(size)
        linked_list = LinkedList()
        linked_list.size = size
        first_range = input("Enter first range: ")
        second_range = input("Enter second range: ")
        first_range, second_range = Validator.is_ranges_correct(first_range, second_range)
        linked_list.generate_array(first_range, second_range)
        self.generate_sequence = linked_list
        return self.generate_sequence

class StrategyGenerateWithReadFromFile(Strategy):
    def generate_list(self):
        sequence = LinkedList()
        file_name = input("Enter file name: ")
        file_name = Validator.validate_file_name(file_name)
        file = open(file_name, 'r')
        content = file.read()
        file_content = content.split(",")
        for elem in file_content:
            if Validator.is_natural(elem) and len(elem) == 4:
                sequence.insert(int(elem))
            else:
                print("Cannot add incorrect value! ")
                continue
        file.close()
        self.generate_sequence = LinkedList(sequence)
        return self.generate_sequence