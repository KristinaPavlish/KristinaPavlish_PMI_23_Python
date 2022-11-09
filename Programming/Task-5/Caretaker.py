from PatientList import PatientList


class Caretaker:
    SIZE = 10

    def __init__(self, _patient_list: PatientList) -> None:
        self.mementos_list = []
        self.patient_list = _patient_list
        self.current_index = 0

    def __str__(self):
        return [str(el) for el in self.mementos_list]

    def __len__(self):
        return len(self.mementos_list)

    def do_undo(self, memento):
        if self.current_index < 2:
            print(self.current_index)
            return "Undo is impossible"

        self.current_index -= 1
        memento.patient_list = self.mementos_list[self.current_index - 1]
        self.patient_list.restore_memento(memento)

    def do_redo(self, memento):
        if self.current_index + 1 > len(self.mementos_list):
            print(self.current_index)
            print(len(self.mementos_list))
            return "Redo is impossible"

        self.current_index += 1
        memento.patient_list = self.mementos_list[self.current_index - 1]
        self.patient_list.restore_memento(memento)


    def backup_memento(self, message, memento) -> None:
        if len(self.mementos_list) == Caretaker.SIZE:
            self.mementos_list.pop(0)
            self.current_index -= 1
        self.mementos_list.append(self.patient_list.save_memento(message, memento))
        self.current_index += 1

