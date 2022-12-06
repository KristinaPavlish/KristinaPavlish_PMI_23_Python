class Logger:

    @staticmethod
    def write_to_file(linked_list_events, file_name="observer.txt"):
        f = open(file_name, 'a')
        f.write(str(linked_list_events) + '\n')
        f.close()


class Observer:

    observer_list = []

    def __init__(self):
        self.observer_list.append(self)
        self.list_for_save_in_file = {}

    def observe(self, event_name, callback=Logger.write_to_file):
        self.list_for_save_in_file[event_name] = callback


class Event:
    def __init__(self, name, list_before, list_now, index=None):
        self.name = name
        self.list_before = list_before
        self.list_now = list_now
        self.index = index

        self.log_event()

    def log_event(self):
        for observer in Observer.observer_list:
            if self.name in observer.list_for_save_in_file:
                observer.list_for_save_in_file[self.name](self)

    def __str__(self):
        return "Event({}, ([ {} ],[ {} ], {} ))".format(self.name, self.list_before, self.list_now, self.index)
