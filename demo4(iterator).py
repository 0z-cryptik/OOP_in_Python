class SequenceIterator:
    """an example of creating an iterator"""

    def __init__(self, sequence):
        # initialize the class
        self._seq = sequence
        self._i = -1

    def __next__(self):
        # increase i
        self._i += 1

        # if i is lower than the length of the sequence, return seq[i]
        if self._i >= len(self._seq):
            raise StopIteration()
        else:
            return self._seq[self._i]

    def __iter__(self):
        # by convention, an iterator must return itself as an iterator
        return self


