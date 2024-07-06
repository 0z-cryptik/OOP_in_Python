from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """Returns the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Returns the item at j"""

    # self holds the sequence instance
    def __contains__(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return True

        return False

    def index(self, i):
        for j in range(len(self)):
            if self[j] == i:
                return j
        raise ValueError("value not in sequence")

    def count(self, val):
        """
        returns the number of times val appears in the sequence
        """
        times = 0

        for i in range(len(self)):
            if self[i] == val:
                times += 1

        return times
    

