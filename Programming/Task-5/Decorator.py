class Decorator:

    def decorator_integer(function):
        def is_integer(number):
            is_item_integer = False
            try:
                if int(number) and int(number) >= 0:
                    is_item_integer = True
            except ValueError:
                print('Item must be integer! ')
                is_item_integer = False
            while not is_item_integer:
                number = input("Enter integer: ")
                continue

        return is_integer

    @staticmethod
    @decorator_integer
    def enter_natural(number):
        return number

    def decorator_natural(function):
        def is_natural(item):
            is_item_natural = False
            while not is_item_natural:
                try:
                    if int(item) <= 0:
                        print("Item must be natural! ")
                        item = input("Enter natural: ")
                        is_item_natural = False
                    else:
                        is_item_natural = True
                except ValueError:
                    print('Item must be natural! ')
                    item = input("Enter natural: ")
            item = int(item)
            return item

        return is_natural

    @staticmethod
    @decorator_natural
    def enter_natural(number):
        return number

    def decorator_word(function):
        def is_only_letter(string):
            is_letter = False
            while not is_letter:
                try:
                    if string.isalpha():
                        is_letter = True
                    else:
                        print("Name must contain only letter ")
                        string = input("Enter again: ")
                        is_letter = False
                except ValueError:
                    print('Word must contain only letter! ')
                    string = input("Enter again: ")
            string = string.title()
            return string

        return is_only_letter

    @staticmethod
    @decorator_word
    def enter_words(string):
        return string

    def decorator_time(function):
        def correct_time(time):
            is_time_correct = False
            while not is_time_correct:
                if time == "00:00":
                    is_time_correct = True
                is_24_hour = False
                split_time = time.split(':')
                if len(split_time) != 2 or len(split_time[0]) != 2 or len(split_time[0]) != 2:
                    print('Time must be XX:XX ')
                    time = input("Enter correct time: ")
                    is_time_correct = False
                    continue
                try:
                    for i in range(0, len(split_time)):
                        if i == 0 and int(split_time[i]) == 24:
                            is_24_hour = True
                        if is_24_hour:
                            if i == 1 and split_time[i] != "00":
                                print("Time incorrect")
                                time = input("Enter correct time: ")
                                is_time_correct = False
                                continue
                        if i == 0 and int(split_time[i]) > 23:
                            print("Time cannot be biggest than 23:59")
                            time = input("Enter correct time: ")
                            is_time_correct = False
                            continue
                        if i == 1 and int(split_time[i]) > 59:
                            print("Minute cannot be biggest than 59")
                            time = input("Enter correct time: ")
                            is_time_correct = False
                            continue
                        if int(split_time[i]) < 0:
                            print("Time must be natural! ")
                            time = input("Enter correct time: ")
                            is_time_correct = False
                            continue
                        if int(split_time[i]) and int(split_time[i]) >= 0:
                            is_time_correct = True
                except ValueError:
                    print('Time must be integer! ')
                    time = input("Enter correct time: ")
                    continue
            return time

        return correct_time

    @staticmethod
    @decorator_time
    def enter_time(time):
        return time

    def decorator_date(function):
        def correct_date(date):
            date = str(date)
            is_date_correct = False
            while not is_date_correct:
                split_date = date.split('/')
                if len(split_date) < 3:
                    print('Date must be XX/XX/XX ')
                    date = input("Enter correct date: ")
                    is_date_correct = False
                    continue
                try:
                    for i in range(0, len(split_date)):
                        if len(split_date[i]) != 2:
                            if i == 0:
                                print('Day must contain 2 digit')
                                date = input("Enter correct time: ")
                                is_date_correct = False
                                continue
                            if i == 1:
                                print('Month must contain 2 digit')
                                date = input("Enter correct date: ")
                                is_date_correct = False
                                continue
                            if i == 2:
                                print('Year must contain 2 digit')
                                date = input("Enter correct date: ")
                                is_date_correct = False
                                continue
                        if i == 0 and int(split_date[i]) > 31:
                            print('Day must be lower than 31')
                            is_date_correct = False
                            date = input("Enter correct date: ")
                            continue
                        if i == 1 and int(split_date[i]) > 12:
                            print('Month must be lower than 12')
                            date = input("Enter correct date: ")
                            is_date_correct = False
                            continue
                        if i == 2 and int(split_date[i]) < 22:
                            print('Year must be biggest than 22')
                            date = input("Enter correct date: ")
                            is_date_correct = False
                            continue

                        if int(split_date[i]) <= 0:
                            print("Time must be natural! ")
                            date = input("Enter correct date: ")
                            is_date_correct = False
                            continue
                        if int(split_date[i]) and int(split_date[i]) >= 0:
                            is_date_correct = True
                except ValueError:
                    print('Time must be integer! ')
                    date = input("Enter correct date: ")
            return str(date)

        return correct_date

    @staticmethod
    @decorator_date
    def enter_date(date):
        return date

    @staticmethod
    def validateFileName():
        def validateFileNameDecorator(func):
            def validateFileNameWrapper(L, filename):
                if not filename:
                    raise ValueError("Incorrect filename.")
                return func(L, filename)

            return validateFileNameWrapper

        return validateFileNameDecorator

