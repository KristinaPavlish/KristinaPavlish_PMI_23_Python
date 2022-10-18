from os.path import exists


class Validate:

    @staticmethod
    def is_integer(item):
        is_item_integer = False
        try:
            if int(item) and int(item) >= 0:
                is_item_integer = True
        except ValueError:
            print('Item must be integer! ')
        return is_item_integer

    @staticmethod
    def is_only_letter(string):
        is_letter = False
        try:
            if string.isalpha():
                is_letter = True
            else:
                print("Name must contain only letter ")
        except ValueError:
            print('Word must contain only letter! ')
        return is_letter

    @staticmethod
    def is_natural(item):
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
    def is_time_correct(time):
        if time == "00:00":
            return True
        is_time_correct = False
        is_24_hour = False
        split_time = time.split(':')
        if len(split_time) != 2 or len(split_time[0]) != 2 or len(split_time[0]) != 2:
            print('Time must be XX:XX ')
            return False
        try:
            for i in range(0, len(split_time)):
                if i == 0 and int(split_time[i]) == 24:
                    is_24_hour = True
                if is_24_hour:
                    if i == 1 and split_time[i] != "00":
                        print("Time incorrect")
                        return False
                if i == 0 and int(split_time[i]) > 23:
                    print("Time cannot be biggest than 23:59")
                    return False
                if i == 1 and int(split_time[i]) > 59:
                    print("Time cannot be biggest than 23:59")
                    return False
                if int(split_time[i]) < 0:
                    print("Time must be natural! ")
                    is_time_correct = False
                if int(split_time[i]) and int(split_time[i]) >= 0:
                    is_time_correct = True
        except ValueError:
            print('Time must be integer! ')
        return is_time_correct

    @staticmethod
    def is_date_correct(date):
        is_date_correct = False
        split_date = date.split('/')
        if len(split_date) < 3:
            is_date_correct = False
            print('Date must be XX/XX/XX ')
            return False
        try:
            for i in range(0, len(split_date)):
                if len(split_date[i]) != 2:
                    if i == 0:
                        print('Day must contain 2 digit')
                        return False
                    if i == 1:
                        print('Month must contain 2 digit')
                        return False
                    if i == 2:
                        print('Year must contain 2 digit')
                        return False
                if i == 0 and int(split_date[i]) > 31:
                    print('Day must be lower than 31')
                    return False
                if i == 1 and int(split_date[i]) > 12:
                    print('Month must be lower than 12')
                    return False
                if i == 2 and int(split_date[i]) < 22:
                    print('Year must be biggest than 22')
                    return False
                if int(split_date[i]) <= 0:
                    print("Time must be natural! ")
                    is_date_correct = False
                if int(split_date[i]) and int(split_date[i]) >= 0:
                    is_date_correct = True
        except ValueError:
            print('Time must be integer! ')
        return is_date_correct

    @staticmethod
    def validate_file_name(file_name):
        while not exists(file_name):
            file_name = input("Enter file name: ")

        return file_name
