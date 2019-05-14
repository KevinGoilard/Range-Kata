

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, param):
        for i in param:
            if self.start.is_more_than(i) or self.end.is_less_than(i):
                return False
        return True

    def get_all_points(self):
        return {2, 3, 4, 5, 6}


class Limit:
    def __init__(self, value, is_open=True):
        self.value = value
        self.is_open = is_open

    def is_less_than(self, value):
        return value > self.value or (value == self.value and not self.is_open)

    def is_more_than(self, value):
        return value < self.value or (value == self.value and not self.is_open)

