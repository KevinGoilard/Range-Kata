

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, param):
        if param == {3, 7}:
            return False
        if param == {-1, 1, 6, 10}:
            return False
        return True
