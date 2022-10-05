def entering_size():
    is_size_correct = False
    size_of_sequence = 0
    # Check entering size correct
    while not is_size_correct:
        try:
            size_of_sequence = int(input("Enter size of array: "))
            if size_of_sequence > 0:
                is_size_correct = True
        except ValueError:
            print('You must enter a valid integer size (size > 0): ')
    return size_of_sequence


def check_is_sequence_correct(sequence_of_numbers, size_of_sequence, first_range, second_range):
    is_numbers_correct = False

    if len(sequence_of_numbers) != size_of_sequence:
        is_numbers_correct = False
        print("Incorrect size of sequence")

    for element in sequence_of_numbers:
        if first_range < element < second_range:
            is_numbers_correct = True
            continue
        else:
            is_numbers_correct = False
            print("Numbers must be < 1000 and > 0")
        break
    return is_numbers_correct


def entering_sequence_numbers():
    size_of_sequence = entering_size()
    sequence_of_numbers = []
    check_entering_sequence_correct = False

    while not check_entering_sequence_correct:
        try:
            sequence_of_numbers = \
                list(map(int,
                         input("Enter " + str(size_of_sequence) + " elements: ")
                         .strip().split()))[:size_of_sequence]
            check_entering_sequence_correct = check_is_sequence_correct(sequence_of_numbers, size_of_sequence, 0, 1000)
        except ValueError:
            print("Element must be number")

    return sequence_of_numbers


def get_index_max_elem(sequence_of_numbers, i, j):
    if len(sequence_of_numbers) > 3:
        first_max_in_sequence = max(sequence_of_numbers[i] + sequence_of_numbers[i + 2],
                                    sequence_of_numbers[j] + sequence_of_numbers[j - 2])
        second_max_in_sequence = max(sequence_of_numbers[i + 1] + sequence_of_numbers[i + 1],
                                     sequence_of_numbers[j] + sequence_of_numbers[j - 3])
    else:
        first_max_in_sequence = sequence_of_numbers[i]
        second_max_in_sequence = sequence_of_numbers[j]
    if first_max_in_sequence > second_max_in_sequence:
        selection_index = i
    else:
        selection_index = j

    return selection_index


def the_winner_of_the_game(sequence_of_numbers):
    first_player_count = 0
    second_player_count = 0

    while len(sequence_of_numbers) != 0:

        # First player
        if len(sequence_of_numbers) == 1:
            first_player_count += sequence_of_numbers[0]
            break
        i = 0
        j = len(sequence_of_numbers) - i - 1
        max_index = get_index_max_elem(sequence_of_numbers, i, j)
        first_player_count += sequence_of_numbers[max_index]
        del sequence_of_numbers[max_index]

        # Second player
        if len(sequence_of_numbers) == 1:
            second_player_count += sequence_of_numbers[0]
            break
        j = len(sequence_of_numbers) - i - 1
        max_index = get_index_max_elem(sequence_of_numbers, i, j)
        second_player_count += sequence_of_numbers[max_index]
        del sequence_of_numbers[max_index]

    if first_player_count > second_player_count:
        return 1
    elif first_player_count < second_player_count:
        return 2
    else:
        return 0


if __name__ == '__main__':
    sequence_of_numbers = entering_sequence_numbers()
    print(the_winner_of_the_game(sequence_of_numbers))
