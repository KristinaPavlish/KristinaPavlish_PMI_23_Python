def entering_array_from_the_keyboard():
    is_numbers_correct = False
    is_size_correct = False
    size_of_elements = 0
    array_of_numbers = []

    # Check entering size correct
    while not is_size_correct:
        try:
            size_of_elements = int(input("Enter size of array: "))
            if size_of_elements > 0:
                is_size_correct = True
        except ValueError:
            print('You must enter a valid integer size (size > 0): ')

    # Check entering array correct
    while not is_numbers_correct:
        try:
            array_of_numbers = \
                list(map(int,
                         input("Enter " + str(size_of_elements) + " numbers: ")
                         .strip().split()))[:size_of_elements]
        except ValueError:
            continue
        if len(array_of_numbers) != size_of_elements:
            is_numbers_correct = 0
            print("Incorrect size of array")
            continue
        unique_elements = (list(set(array_of_numbers)))
        if len(unique_elements) != len(array_of_numbers):
            is_numbers_correct = False
            print("Numbers must be unique")
            continue
        for element in array_of_numbers:
            if int(element):
                is_numbers_correct = True
                continue
            else:
                is_numbers_correct = False
                print("Numbers must be natural and four-digit")
                break

    return array_of_numbers


def entering_array_with_random_elements():
    global first_range, second_range, size_of_array
    import random
    is_size_correct = False
    is_first_range_correct = False
    is_second_range_correct = False

    # Check entering size correct
    while not is_size_correct:
        try:
            size_of_array = int(input("Enter size of array( > 0 ): "))
            if size_of_array > 0:
                is_size_correct = True
        except ValueError:
            print('You must enter a valid integer size (size > 0): ')
    print("Range (a < ... < b) ")
    while not is_first_range_correct:
        try:
            first_range = int(input("Enter a : "))
            is_first_range_correct = True
        except ValueError:
            print("Please, provide integer number")
        continue

    while not is_second_range_correct:
        try:
            second_range = int(input("Enter b : "))
            if second_range > first_range and second_range - first_range >= size_of_array:
                is_second_range_correct = True
            else:
                print("b must be more than a by " + str(size_of_array) + " elements ")
        except ValueError:
            print("Please, provide integer number and biggest than a")
        continue

    random_list = random.sample(range(first_range, second_range), size_of_array)

    return random_list


def bubble_sort(array):
    size = len(array)
    swapped = False
    count_swaps = 0
    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
                count_swaps += 1
        if not swapped:
            return

    print("Count of swapping: " + str(count_swaps))
    return array


def binary_search(array):
    sorted_array = bubble_sort(array)
    print(sorted_array)
    is_element_to_find_correct = False
    number_to_find = 0
    # Check entering element correct
    while not is_element_to_find_correct:
        try:
            number_to_find = int(input("Element to find: "))
            is_element_to_find_correct = True
        except ValueError:
            print('Please, provide integer number')

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
            entered_array = entering_array_from_the_keyboard()
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
        print("[3] - Exit")
        number = input("Enter option : ")
        if number == str(1):
            array_sorted = bubble_sort(input_array)
            print(array_sorted)
        if number == str(2):
            array_for_search = binary_search(input_array)
            print(array_for_search)
        if number == str(3):
            break


if __name__ == '__main__':
    menu()
