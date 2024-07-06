# Write a Python class that extends the Progression class so that each value in the progression is the square root of the previous value. (Note that you can no longer represent each value with an integer.) Your constructor should accept an optional parameter specifying the start value, using 65,536 as a default.

import os, sys

grandparent_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../python_DSA")
)

sys.path.append(grandparent_folder)

from demo7_progression import Progression

class CustomProgression(Progression):
    def __init__(self, start=65563) -> None:
        super().__init__(start)

    def _advance(self):
        self._current = self._current ** 2


if __name__ == '__main__':
    mi_progression = CustomProgression(2)
    mi_progression.print_progression(8)

        
