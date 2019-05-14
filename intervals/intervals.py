

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, param):
        for i in param:
            if i < self.start.value or i > self.end.value or (i == self.end.value and not self.end.is_open):
                return False
        return True


class Limit:
    def __init__(self, value, is_open=True):
        self.value = value
        self.is_open = is_open
