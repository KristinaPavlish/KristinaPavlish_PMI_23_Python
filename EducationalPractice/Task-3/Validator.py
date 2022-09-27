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
                is_integer = Validator.is_integer(str_element)
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
