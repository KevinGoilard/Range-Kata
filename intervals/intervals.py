

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
        return set(range(self.start.get_point(), self.end.get_point() + 1))

    def end_points(self):
        return [self.start.get_point(), self.end.get_point()]

    def contains_interval(self, other):
        return self.contains(other.get_all_points())

    def equals(self, other):
        return self.start.equals(other.start) and self.end.equals(other.end)


class Limit:
    def __init__(self, value, is_open=True):
        self.value = value
        self.is_open = is_open

    def is_less_than(self, value):
        return value > self.value or (value == self.value and self.is_open)

    def is_more_than(self, value):
        return value < self.value or (value == self.value and self.is_open)

    def get_point(self):
        pass

    def equals(self, other):
        if type(self) != type(other):
            return False
        return self.value == other.value and self.is_open == other.is_open


class StartLimit(Limit):
    def get_point(self):
        return self.value + self.is_open


class EndLimit(Limit):
    def get_point(self):
        return self.value - self.is_open
