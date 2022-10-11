from Validator import Validator
from LinkedList import LinkedList


class Strategy:

    def __init__(self, generate_sequence=None):
        self.generate_sequence = generate_sequence

    def get_list(self):
        linked_list = LinkedList()
        if self.generate_sequence is not None:
            linked_list = self.generate_sequence()
            print(linked_list)
        return linked_list


def generate_with_generator():
    size = input("Enter size: ")
    is_index_correct = Validator.is_natural(size)
    while not is_index_correct:
        size = input("Enter correct size: ")
        is_index_correct = Validator.is_natural(size)
    size = int(size)
    linked_list = LinkedList()
    linked_list.size = size
    linked_list.generate_list_with_generator(size)
    return linked_list


def generate_with_read_from_file():
    sequence = LinkedList()
    file_name = input("Enter file name: ")
    Validator.validate_file_name(file_name)
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
    return LinkedList(sequence)


