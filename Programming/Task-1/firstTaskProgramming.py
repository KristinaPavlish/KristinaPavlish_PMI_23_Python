def entering_array():
    is_numbers_correct = False
    is_size_correct = False
    size_of_array = 0
    array_of_numbers = []

    # Check entering size correct
    while not is_size_correct:
        size_of_array = input("Enter size of array: ")
        if int(size_of_array) > 0:
            is_size_correct = True
        else:
            print('You must enter a valid size (size > 0): ')

        size_of_array = int(size_of_array)

    # Check entering array correct
    while not is_numbers_correct:
        try:
            array_of_numbers = \
                list(map(int,
                         input("Enter " + str(size_of_array) + " numbers: ")
                         .strip().split()))[:size_of_array]
        except ValueError:
            continue
        if len(array_of_numbers) != size_of_array:
            is_numbers_correct = 0
            print("Incorrect size of array")
            continue
        for element in array_of_numbers:
            if isinstance(element, int):
                if 999 < int(element) <= 9999:
                    is_numbers_correct = True
                    continue
                else:
                    is_numbers_correct = False
                    print("Numbers must be natural and four-digit")
                break

    return array_of_numbers


def compress_the_array(array_of_numbers):
    array_after_compression = []

    for i in range(0, len(array_of_numbers)):
        number = array_of_numbers[i]
        first_digit = str(number)[0]
        second_digit = str(number)[1]
        third_digit = str(number)[2]
        fourth_digit = str(number)[3]

        if first_digit == third_digit and second_digit == fourth_digit and first_digit != second_digit:
            array_after_compression.append(number)
            continue

        elif first_digit == fourth_digit and second_digit == third_digit and first_digit != second_digit:
            array_after_compression.append(number)
            continue
        else:
            array_after_compression.append(0)
            continue

    first_not_null = 0
    for i in range(0, len(array_after_compression)):
        if array_after_compression[len(array_after_compression)-i-1] != 0:
            first_not_null = len(array_after_compression)-i-1
            break

    for i in range(0, len(array_after_compression)):
        if i < first_not_null and array_after_compression[i] == 0:
            del array_after_compression[i]

    return array_after_compression


if __name__ == '__main__':
    input_array = entering_array()
    print("Input array:")
    print(input_array)

    result = compress_the_array(input_array)
    print("Output array:")
    print(result)