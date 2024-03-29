from os.path import exists
FIRST_RANGE = 999
SECOND_RANGE = 9999

class Validator:

    @staticmethod
    def is_natural(item):
        is_item_natural = False
        try:
            if int(item) <= 0:
                print("item must be natural! ")
                is_item_natural = False
            if int(item) and int(item) >= 0:
                is_item_natural = True
        except ValueError:
            print('item must be integer! ')
        return is_item_natural

    @staticmethod
    def is_array_contain_int_only(array):
        array = array.split()
        is_integer = True
        for str_element in array:
            if not is_integer:
                return is_integer
            else:
                is_integer = Validator.is_natural(str_element)
        return is_integer

    @staticmethod
    def is_length_correct(value, acceptable_lower=None, acceptable_upper=None):
        if acceptable_lower is None:
            acceptable_lower = FIRST_RANGE
        if acceptable_upper is None:
            acceptable_upper = SECOND_RANGE
        is_numbers_correct = False
        if acceptable_lower < int(value) <= acceptable_upper:
            is_numbers_correct = True
        else:
            is_numbers_correct = False
            print("Number must be in range [" + str(acceptable_lower) + " , " + str(acceptable_upper) + "]")
        return is_numbers_correct

    @staticmethod
    def is_ranges_correct(first_range, second_range):
        is_first_range_correct = Validator.is_natural(first_range)
        while not is_first_range_correct:
            first_range = input("Enter correct first range: ")
            is_first_range_correct = Validator.is_natural(first_range)
        first_range = int(first_range)
        is_second_range_correct = Validator.is_natural(second_range)
        while not is_second_range_correct:
            second_range = input("Enter correct second range: ")
            is_second_range_correct = Validator.is_natural(second_range)
        second_range = int(second_range)
        return first_range, second_range

    @staticmethod
    def validate_file_name(file_name):
        while not exists(file_name):
            file_name = input("Enter file name: ")
        return file_name