# The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator. Implement a class named ReversedSequenceIterator that serves as a reverse iterator for any Python sequence type. The first call to next should return the last element of the sequence, the second call to next should return the second-to-last element, and so forth.


class ReverseSequenceIterator:
    """an example of creating an iterator"""

    def __init__(self, sequence):
        # initialize the class
        self._seq = sequence
        # for the reverse iterator
        self._i = 0
        # to keep up with the length of the sequence
        self._k = -1

    def __next__(self):
        # reduce i
        self._i -= 1
        self._k += 1

        # if i is lower than the length of the sequence, return seq[i]
        if self._k >= len(self._seq):
            raise StopIteration()
        else:
            return self._seq[self._i]

    def __iter__(self):
        # by convention, an iterator must return itself as an iterator
        return self


if __name__ == "__main__":
    mi_string = "abcde"
    
    mi_seq = ReverseSequenceIterator(mi_string)
    count = 0

    for item in mi_seq:
        print(item)
