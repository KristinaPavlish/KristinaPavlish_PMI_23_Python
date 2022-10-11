from Node import Node
from Validator import Validator
from LinkedListIterator import LinkedListIterator
from LinkedListGenerator import LinkedListGenerator

import random

FIRST_RANGE = 999
SECOND_RANGE = 9999


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.size = None
        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __getitem__(self, index):
        i = 0
        temp = self.head

        if type(index) is int:
            while temp is not None:
                if i == index:
                    return temp.value
                temp = temp.next
                i += 1

    @property
    def values(self):
        return [node.value for node in self]

    def insert(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple_nodes(self, values):
        for value in values:
            self.insert(value)

    def insert_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def add_str_element_in_position(self, new_str_element, position, is_zero_values_enable=None):
        is_valid = True
        if not is_zero_values_enable:
            is_valid = Validator.is_natural(new_str_element) and Validator.is_length_correct(new_str_element)
        if is_valid:
            new_node = Node(new_str_element)
            if position < 1:
                print("\nposition should be >= 1.")
            elif position == 1:
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                for i in range(1, position - 1):
                    if temp is not None:
                        temp = temp.next
                if temp is not None:
                    new_node.next = temp.next
                    temp.next = new_node
                else:
                    print("\nThe previous node is null.")

    def delete_str_element_by_position(self, position):
        node_to_delete = None
        if position < 1:
            print("\nposition should be >= 1.")
        elif position == 1 and self.head is not None:
            node_to_delete = self.head
            self.head = self.head.next
            node_to_delete = None
        else:
            temp = self.head
            for i in range(1, position - 1):
                if temp is not None:
                    temp = temp.next
            if temp is not None and temp.next is not None:
                node_to_delete = temp.next
                temp.next = temp.next.next
                node_to_delete = None
            else:
                print("\nThe node is already null.")

    def delete_str_element_by_two_position(self, first_position, second_position):
        if first_position < 1 or second_position < 1 or first_position == second_position or first_position > second_position:
            print("Incorrect position ")
        elif first_position == 0 and second_position == 1 and self.head is not None:
            self.head = self.head.next
        else:
            temp = self.head
            i = first_position
            while i != second_position + 1:
                if temp is not None:
                    temp = temp.next
                    i += 1
            if temp is not None and temp.next is not None:
                temp.next = temp.next.next
            else:
                print("\nThe node is already null.")

    def delete_all_list(self):
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def enter_size(self):
        size = input("Enter size of array: ")
        is_size_correct = Validator.is_natural(size)
        while not is_size_correct:
            size = input("Enter correct size: ")
            is_size_correct = Validator.is_natural(size)
        self.size = int(size)

    def entering_list(self):
        while len(self) != self.size:
            data = input('Enter data item: ')
            if Validator.is_natural(data) and Validator.is_length_correct(data):
                self.insert(int(data))

    def generate_array(self, lower=None, upper=None):
        if lower is None:
            lower = FIRST_RANGE
        if upper is None:
            upper = SECOND_RANGE
        while len(self) != self.size:
            data = random.randint(lower, upper)
            self.insert(data)

    def generate_list_with_generator(self, size):
        linked_list_generator = LinkedListGenerator(self)
        generator = linked_list_generator.generator_random()
        self.delete_all_list()
        if len(self) + size <= size:
            for i in range(0, self.size):
                value = next(generator)
        return self


    @staticmethod
    def check_pattern_xyxy(str_element):
        first_digit = str_element[0]
        second_digit = str_element[1]
        is_number_pattern = True

        # position for X
        first_pos = len(str_element) - 2
        # position for Y
        second_pos = len(str_element) - 1

        # check incorrect pattern XXXX
        if first_digit == second_digit:
            is_number_pattern = False
            return is_number_pattern

        while first_pos != 0 and second_pos != 1:
            if int(first_digit) == int(str_element[first_pos]) and int(second_digit) == int(str_element[second_pos]):
                is_number_pattern = True
                first_pos = first_pos - 2
                second_pos = second_pos - 2
            else:
                is_number_pattern = False
                return is_number_pattern

        return is_number_pattern

    @staticmethod
    def check_pattern_xyyx(str_element):
        first_digit = str_element[0]
        second_digit = str_element[1]
        is_number_pattern = True

        # check incorrect pattern XXXX
        if first_digit == second_digit:
            is_number_pattern = False
            return is_number_pattern

        # check the length of the str_element and find the position
        # to which to check all X
        if len(str_element) % 4 == 0:
            pos = len(str_element) - 2

        elif len(str_element) % 2 == 0 and len(str_element) % 4 != 0:
            length = len(str_element) // 4
            pos = length - 1

        elif len(str_element) % 3 == 0:
            pos = len(str_element) - 3

        else:
            pos = len(str_element) - 1

        if len(str_element) == 4:
            pos = len(str_element) - 1

        # check all X
        while pos != 0:
            if int(first_digit) == int(str_element[pos]):
                is_number_pattern = True
                pos = pos - 3
            else:
                is_number_pattern = False
                return is_number_pattern

        # create new string without X
        another_digits = ""
        for digit in str_element:
            if digit != first_digit:
                another_digits += digit
            else:
                continue

        # check all Y
        for digit in another_digits:
            if digit == second_digit:
                is_number_pattern = True
            else:
                is_number_pattern = False
                return is_number_pattern

        return is_number_pattern

    def compress_the_array(self):
        index = 1
        for str_element in self:
            string_str_element = str(str_element)
            is_valid = self.check_pattern_xyxy(string_str_element) or self.check_pattern_xyyx(string_str_element)

            if not is_valid:
                self.delete_str_element_by_position(index)
                self.add_str_element_in_position(0, index, True)
                index += 1
                continue
            if is_valid:
                index += 1

        first_not_null = 0

        i = len(self) - 1
        while i >= 0:
            if self[i] != 0:
                first_not_null = i
                break
            i -= 1

        current_index = 1
        while True:
            if first_not_null == 0:
                break
            if self[current_index - 1] == 0 and current_index <= first_not_null:
                self.delete_str_element_by_position(current_index)
                i = len(self) - 1
                while i >= 0:
                    if self[i] != 0:
                        first_not_null = i
                        break
                    i -= 1
            else:
                current_index += 1

            if self[current_index] is None:
                break