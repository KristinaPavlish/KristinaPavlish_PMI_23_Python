def entering_sequence_numbers():
    is_numbers_correct = 0
    is_size_correct = False
    size_of_sequence = 0
    sequence_of_numbers = []

    # Check entering size correct
    while not is_size_correct:
        size_of_sequence = input("Enter size of sequence: ")
        if int(size_of_sequence) > 0:
            is_size_correct = True
        else:
            print('You must enter a valid size (size > 0): ')

        size_of_sequence = int(size_of_sequence)

    # Check entering sequence correct
    while is_numbers_correct == 0:
        sequence_of_numbers = \
            list(map(int,
                     input("Enter " + str(size_of_sequence) + " elements: ")
                     .strip().split()))[:size_of_sequence]
        if len(sequence_of_numbers) != size_of_sequence:
            is_numbers_correct = 0
            print("Incorrect size of sequence")
            continue
        for element in sequence_of_numbers:
            if 0 < element < 1000:
                is_numbers_correct = 1
                continue
            else:
                is_numbers_correct = 0
                print("Numbers must be < 1000 and > 0")
            break

    return sequence_of_numbers


def get_index_max_elem(sequence_of_numbers, i, j):
    max_in_sequence = max(sequence_of_numbers[i], sequence_of_numbers[j])
    selection_index = 0

    if sequence_of_numbers[j] == max_in_sequence:
        selection_index = j

    if sequence_of_numbers[i] == max_in_sequence:
        selection_index = i
    return selection_index


def the_winner_of_the_game():
    first_player_count = 0
    second_player_count = 0
    sequence_of_numbers = entering_sequence_numbers()

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
    print(the_winner_of_the_game())
