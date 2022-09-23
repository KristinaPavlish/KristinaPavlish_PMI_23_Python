FIRST_RANGE = 999
SECOND_RANGE = 9999


def check_the_element_is_natural(element):
    is_element_natural = False
    try:
        if int(element) <= 0:
            print("Element must be natural! ")
            is_element_natural = False
        if int(element) and int(element) >= 0:
            is_element_natural = True
    except ValueError:
        print('Element must be integer! ')
    return is_element_natural


def enter_size():
    size = input("Enter size of array: ")
    is_size_correct = check_the_element_is_natural(size)
    while not is_size_correct:
        size = input("Enter correct size: ")
        is_size_correct = check_the_element_is_natural(size)
    return int(size)


def check_is_array_contain_only_int(str_array):
    array = str_array.split()
    is_integer = True
    for element in array:
        if not is_integer:
            return is_integer
        else:
            is_integer = check_the_element_is_natural(element)

    return is_integer


def check_entered_correct_count_of_numbers(size, array):
    is_sizes_correct = size == len(array)
    return is_sizes_correct


def check_is_elements_in_correct_range(array):
    is_numbers_correct = True
    for element in array:
        if FIRST_RANGE < int(element) <= SECOND_RANGE:
            is_numbers_correct = True
            continue
        else:
            is_numbers_correct = False
            print("Numbers must be in range [" + str(FIRST_RANGE) + " , " + str(SECOND_RANGE) + "]")
        break
    return is_numbers_correct


def is_array_correct(size, array):
    is_valid = \
        check_is_array_contain_only_int(array) \
        and check_is_elements_in_correct_range(array) \
        and check_entered_correct_count_of_numbers(size, array)
    return is_valid


def entering_array():
    size_of_array = enter_size()
    is_numbers_correct = False
    array = []
    while not is_numbers_correct:
        str_array = input("Enter " + str(size_of_array) + " elements: ")

        if check_is_array_contain_only_int(str_array):
            array = [int(ele) for ele in str_array.split()]
            is_numbers_correct = False
        else:
            print("Array must contain integer values")
            continue

        if check_entered_correct_count_of_numbers(size_of_array, array):
            is_numbers_correct = False
        else:
            print("Incorrect size of array")
            continue

        if check_is_elements_in_correct_range(array):
            is_numbers_correct = True
        else:
            print("Element is not in correct range")

    return array


def entering_random_array():
    size_of_array = enter_size()
    import random
    random_list = random.sample(range(FIRST_RANGE, SECOND_RANGE), size_of_array)
    return random_list


def check_pattern_xyxy(element):
    first_digit = element[0]
    second_digit = element[1]
    is_number_pattern = True

    # position for X
    first_pos = len(element) - 2
    # position for Y
    second_pos = len(element) - 1

    # check incorrect pattern XXXX
    if first_digit == second_digit:
        is_number_pattern = False
        return is_number_pattern

    while first_pos != 0 and second_pos != 1:
        if int(first_digit) == int(element[first_pos]) and int(second_digit) == int(element[second_pos]):
            is_number_pattern = True
            first_pos = first_pos - 2
            second_pos = second_pos - 2
        else:
            is_number_pattern = False
            return is_number_pattern

    return is_number_pattern


def check_pattern_xyyx(element):
    first_digit = element[0]
    second_digit = element[1]
    is_number_pattern = True

    # check incorrect pattern XXXX
    if first_digit == second_digit:
        is_number_pattern = False
        return is_number_pattern

    # check the length of the element and find the position
    # to which to check all X
    if len(element) % 4 == 0:
        pos = len(element) - 2

    elif len(element) % 2 == 0 and len(element) % 4 != 0:
        length = len(element) // 4
        pos = length - 1

    elif len(element) % 3 == 0:
        pos = len(element) - 3

    else:
        pos = len(element) - 1

    if len(element) == 4:
        pos = len(element) - 1

    # check all X
    while pos != 0:
        if int(first_digit) == int(element[pos]):
            is_number_pattern = True
            pos = pos - 3
        else:
            is_number_pattern = False
            return is_number_pattern

    # create new string without X
    another_digits = ""
    for digit in element:
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


def compress_the_array(array_of_numbers):
    array_after_compression = []

    for element in array_of_numbers:
        string_element = str(element)
        if check_pattern_xyxy(string_element) or check_pattern_xyyx(string_element):
            array_after_compression.append(element)
            continue
        else:
            array_after_compression.append(0)
            continue

    last_not_null = 0
    index = len(array_after_compression)
    while index != 0:
        index = index - 1
        if array_after_compression[index] != 0:
            last_not_null = index
            break

    new_list = []
    count_zero = len(array_after_compression) - last_not_null - 1

    # delete zero
    for i in range(0, last_not_null + 1):
        if array_after_compression[i] != 0:
            new_list.append(array_after_compression[i])

    # add zero in the end
    if len(new_list) == 0:
        for i in range(0, len(array_after_compression)):
            new_list.append(0)
    else:
        for i in range(0, count_zero):
            new_list.append(0)
    return new_list


def menu():
    while 1 == 1:
        print("MENU:")
        print("[1] - Enter element from keyboard ")
        print("[2] - Generate an arbitrary array")
        print("[3] - Exit")
        number = input("Enter option : ")
        if number == str(1):
            entered_array = entering_array()
            what_to_do_with_array(entered_array)
        if number == str(2):
            random_array = entering_random_array()
            what_to_do_with_array(random_array)
        if number == str(3):
            break


def what_to_do_with_array(array):
    while 1 == 1:
        input_array = array.copy()
        print("MENU:")
        print("[1] - Show array")
        print("[2] - Show compressed array")
        print("[3] - Go to entering array")
        number = input("Enter option : ")
        if number == str(1):
            print(input_array)
        if number == str(2):
            array_for_compress = compress_the_array(input_array)
            print(array_for_compress)
        if number == str(3):
            break


if __name__ == '__main__':
    menu()
