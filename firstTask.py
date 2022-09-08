def the_winner_of_the_game(size_of_sequence):
    first_player_count = 0
    second_player_count = 0
    is_numbers_correct = 0
    sequence_of_numbers = []

    # Check entering correct
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

    print(sequence_of_numbers)
    while len(sequence_of_numbers) != 0:
        # First player
        if len(sequence_of_numbers) == 1:
            first_player_count += sequence_of_numbers[0]
            break
        i = 0
        j = len(sequence_of_numbers) - i - 1
        max_in_sequence = max(sequence_of_numbers[i], sequence_of_numbers[j])
        selection_index = 0

        if sequence_of_numbers[j] == max_in_sequence:
            selection_index = j

        if sequence_of_numbers[i] == max_in_sequence:
            selection_index = i

        first_player_count += max_in_sequence
        del sequence_of_numbers[selection_index]

        # Second player
        if len(sequence_of_numbers) == 1:
            second_player_count += sequence_of_numbers[0]
            break

        j = len(sequence_of_numbers) - i - 1
        max_in_sequence = max(sequence_of_numbers[i], sequence_of_numbers[j])
        selection_index = 0

        if sequence_of_numbers[j] == max_in_sequence:
            selection_index = j

        if sequence_of_numbers[i] == max_in_sequence:
            selection_index = i

        second_player_count += max_in_sequence
        del sequence_of_numbers[selection_index]

    print("First Player points:" + str(first_player_count))
    print("Second Player points:" + str(second_player_count))
    if first_player_count > second_player_count:
        print(1)
    elif first_player_count < second_player_count:
        print(2)
    else:
        print(0)


if __name__ == '__main__':
    the_winner_of_the_game(5)
