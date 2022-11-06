from os.path import exists


class Validate:

    @staticmethod
    def is_natural_elem(item):
        is_item_natural = False
        try:
            if int(item) <= 0:
                print("Item must be natural! ")
                is_item_natural = False
            if int(item) and int(item) >= 0:
                is_item_natural = True
        except ValueError:
            print('Item must be integer! ')
        return is_item_natural

    @staticmethod
    def validate_file_name(file_name):
        while not exists(file_name):
            file_name = input("Enter file name: ")

        return file_name