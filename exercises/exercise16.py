# In Section 2.3.5, we note that our version of the Range class has implicit support for iteration, due to its explicit support of both __len__ and __getitem__. The class also receives implicit support of the Boolean test, “k in r” for Range r. This test is evaluated based on a forward iteration through the range, as evidenced by the relative quickness of the test 2 in Range(10000000) versus 9999999 in Range(10000000). Provide a more efficient implementation of the __contains__ method to determine whether a particular value lies within a given range. The running time of your method should be independent of the length of the range.

import os, sys

grandparent_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../python_DSA")
)

sys.path.append(grandparent_folder)

from demo5_Range import Range


class CustomRange(Range):
    def __init__(self, start, stop=None, step=1):
        super().__init__(start, stop, step)

    def __contains__(self, num: int):
        if self._step > 0:
            if num < self._start or num >= self._stop:
                return False

        # for a range of negative numbers
        else:
            if num > self._start or num <= self._stop:
                return False

        if (num - self._start) % self._step == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    mi_range1 = CustomRange(-1, -10, -3)
    print(mi_range1.__contains__(-4))

    mi_range2 = CustomRange(2, 20, 3)
    print(mi_range2.__contains__(6))
