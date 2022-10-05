
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


def check_the_element_is_float(element):
    is_element_float = False
    try:
        if float(element):
            is_element_float = True
    except ValueError:
        print('Element must be float or integer! ')
    return is_element_float


def enter_size():
    size = input("Enter size of array: ")
    is_size_correct = check_the_element_is_natural(size)
    while not is_size_correct:
        size = input("Enter correct size: ")
        is_size_correct = check_the_element_is_natural(size)
    return int(size)


def check_is_array_contain_only_float(str_array):
    array = str_array.split()
    is_float = True
    for element in array:
        if not is_float:
            return is_float
        else:
            is_float = check_the_element_is_float(element)

    return is_float


def check_entered_correct_count_of_numbers(size, array):
    is_sizes_correct = size == len(array)
    return is_sizes_correct


def is_elements_unique(array_of_numbers):
    unique_elements = (list(set(array_of_numbers)))
    if len(unique_elements) == len(array_of_numbers):
        is_numbers_correct = True
    else:
        is_numbers_correct = False
        return is_numbers_correct
    return is_numbers_correct


def is_ranges_correct(first_range, second_range, size_of_array):
    is_range_correct = False

    if check_the_element_is_float(first_range) and check_the_element_is_float(second_range):
        if float(second_range) > float(first_range) and float(second_range) - float(first_range) >= float(size_of_array):
            is_range_correct = True
        else:
            print("b must be more than a by " + str(size_of_array) + " elements ")
            is_range_correct = False
    return is_range_correct


def entering_array():
    size_of_array = enter_size()
    is_numbers_correct = False
    array = []
    while not is_numbers_correct:
        str_array = input("Enter " + str(size_of_array) + " elements: ")

        if check_is_array_contain_only_float(str_array):
            array = [float(ele) for ele in str_array.split()]
            is_numbers_correct = False
        else:
            print("Array must contain float values")
            continue

        if check_entered_correct_count_of_numbers(size_of_array, array):
            is_numbers_correct = False
        else:
            print("Incorrect size of array")
            continue

        if is_elements_unique(array):
            is_numbers_correct = True
        else:
            print("Numbers must be unique")

    return array


def entering_array_with_random_elements():
    import random
    size_of_array = enter_size()
    is_range_correct = False
    first_range = 0
    second_range = 0
    print("Range (a < ... < b) ")

    while not is_range_correct:
        first_range = input("Enter a: ")
        second_range = input("Enter b: ")
        if is_ranges_correct(first_range, second_range, size_of_array):
            is_range_correct = True

    random_list = random.sample(range(int(first_range), int(second_range)), size_of_array)

    return random_list


def bubble_sort(array):
    size = len(array)
    swapped = False
    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            return
    return array


def count_operations_for_bubble_sort(array):
    size_of_array = len(array)
    swapped = False
    count_swaps = 0
    for i in range(size_of_array - 1):
        for j in range(0, size_of_array - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
                count_swaps += 1
        if not swapped:
            return

    return count_swaps


def binary_search(array):
    sorted_array = bubble_sort(array)
    is_element_to_find_correct = False
    number_to_find = 0

    # Check entering element correct
    while not is_element_to_find_correct:
        number_to_find = input("Enter number to find: ")
        if check_the_element_is_float(number_to_find):
            is_element_to_find_correct = True

    number_to_find = float(number_to_find)
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = low + (high - low) // 2

        if sorted_array[middle] == number_to_find:
            return middle
        elif sorted_array[middle] < number_to_find:
            low = middle + 1
        else:
            high = middle - 1
    return -1


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
            random_array = entering_array_with_random_elements()
            what_to_do_with_array(random_array)
        if number == str(3):
            break


def what_to_do_with_array(array):
    while 1 == 1:
        input_array = array.copy()
        print("MENU:")
        print("[1] - Show sorted array")
        print("[2] - Find index entered element using binary search")
        print("[3] - Show the number of operations for bubble sort")
        print("[4] - Go to entering array")
        number = input("Enter option : ")
        if number == str(1):
            array_sorted = bubble_sort(input_array)
            print(array_sorted)
        if number == str(2):
            array_for_search = binary_search(input_array)
            print(array_for_search)
        if number == str(3):
            count_operations = count_operations_for_bubble_sort(input_array)
            print("Count: ", count_operations)
        if number == str(4):
            break


if __name__ == '__main__':
    menu()
