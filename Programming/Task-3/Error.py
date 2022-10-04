class Error(Exception):
    pass


class ValueIncorrect(Error):
    def __init__(self, message="Value incorrect"):
        self.message = message
        super().__init__(self.message)
