import random

FIRST_RANGE = 999
SECOND_RANGE = 9999


class LinkedListGenerator:
    def __init__(self, list):
        self.list = list

    def generator_random(self, lower=None, upper=None):
        if lower is None:
            lower = FIRST_RANGE
        if upper is None:
            upper = SECOND_RANGE
        if len(self.list) == 0:
            num = random.randint(lower, upper)
            self.list.insert(num)
            yield num
        while self.list is not StopIteration and len(self.list) < self.list.size:
            num = random.randint(lower, upper)
            self.list.insert(num)
            yield num

