DEFAULT_SIZE_MATRIX = 10


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
    size = input("Enter size of matrix: ")
    is_size_correct = check_the_element_is_natural(size)
    while not is_size_correct:
        size = input("Enter correct size: ")
        is_size_correct = check_the_element_is_natural(size)
    return int(size)


def print_matrix(matrix):
    for elem in matrix:
        for i in range(0, len(elem)):
            print(str(elem[i]) + "\t", end=" ")
        print("\n")


def custom_print_matrix(matrix):
    if len(matrix) >= 7:
        matrix_for_print = []
        for i in range(0, len(matrix)):
            if i <= 2 or len(matrix) - 2 <= i:
                matrix_for_print.append(matrix[i])
            if i == 2:
                matrix_for_print.append(["..." for y in range(len(matrix))])
        matrix_for_print_2 = [[] for i in range(len(matrix_for_print))]
        for i in range(0, len(matrix_for_print)):
            for j in range(0, len(matrix_for_print[i])):

                if j == 3:
                    matrix_for_print_2[i].append("...")
                if j < 3 or j > len(matrix_for_print[i]) - 4:
                    matrix_for_print_2[i].append(matrix_for_print[i][j])
        print_matrix(matrix_for_print_2)
    else:
        print_matrix(matrix)


def generate_matrix(size):
    count_of_operations = 0
    matrix = [[0 for x in range(size)] for y in range(size)]
    for i in range(0, size):
        for j in range(0, i + 1):
            if i == j:
                matrix[i][j] = size
            if i > j:
                matrix[i][j] = size - (i - j)
            count_of_operations += 1
    print("Count of steps for generate:" + str(count_of_operations))
    custom_print_matrix(matrix)


def menu():
    entered_size = DEFAULT_SIZE_MATRIX
    while 1 == 1:
        print("MENU:")
        print("[1] - Enter size of matrix ")
        print("[2] - Generate matrix")
        print("[3] - Exit")
        number = input("Enter option : ")
        if number == str(1):
            entered_size = enter_size()
        if number == str(2):
            generate_matrix(entered_size)
        if number == str(3):
            break


if __name__ == '__main__':
    menu()
