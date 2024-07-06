# Write a Python class that extends the Progression class so that each value in the progression is the absolute value of the difference between the previous two values. You should include a constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults.

import os, sys

grandparent_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../python_DSA")
)

sys.path.append(grandparent_folder)

from demo7_progression import Progression


class CustomProgression(Progression):
    def __init__(self, first=2, second=200) -> None:
        super().__init__(first)
        # initial prev, will be reassigned to current value in the advance method
        self._prev = second + first

    def _advance(self):
        self._prev, self._current = self._current, abs(self._current - self._prev)


if __name__ == "__main__":
    mi_progression = CustomProgression(1,6)
    mi_progression.print_progression(7)
