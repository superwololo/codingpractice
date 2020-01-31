import heapq


class MedianCounter(object):
    def __init__(self):
        self.lower = [] # The sign of these values is flipped
        self.upper = []

    def median(self):
        if len(self.lower) == 0:
            return None
        elif len(self.lower) > len(self.upper):
            return self._max_lower()
        elif len(self.lower) < len(self.upper):
            return self._min_upper()
        else:
            return float(self._max_lower() + self._min_upper()) / 2

    def _add_lower(self, elem):
        heapq.heappush(self.lower, -elem)

    def _add_upper(self, elem):
        heapq.heappush(self.upper, elem)

    def _max_lower(self):
        return -self.lower[0]

    def _min_upper(self):
        if len(self.upper) == 0:
            return None
        return self.upper[0]

    def add(self, elem):
        if len(self.lower) == 0:
            self._add_lower(elem)
        elif len(self.lower) == len(self.upper):
            if elem < self._min_upper():
                self._add_lower(elem)
            else:
                self._add_upper(elem)
        elif len(self.lower) > len(self.upper):
            if elem < self._max_lower():
                self._add_upper(-heapq.heappop(self.lower))
                self._add_lower(elem)
            else:
                self._add_upper(elem)
        elif len(self.upper) > len(self.lower):
            if elem > self._min_upper():
                self._add_lower(heapq.heappop(self.upper))
                self._add_upper(elem)
            else:
                self._add_lower(elem)


if __name__ == '__main__':
    counter = MedianCounter()
    stream = range(1, 10)
    for elem in stream:
        counter.add(elem)
        print counter.median()
