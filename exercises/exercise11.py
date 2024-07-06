# The collections.Sequence abstract base class does not provide support for comparing two sequences to each other. Modify our Sequence class from Code Fragment 2.14 to include a definition for the __eq__ method, so that expression seq1 == seq2 will return True precisely when the two sequences are element by element equivalent.

import os, sys

grandparent_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../python_DSA")
)

sys.path.append(grandparent_folder)

from demo8_abstract_method import Sequence


class CustomSequence(Sequence):
    def __init__(self, seq) -> None:
        super().__init__()
        self._sequence = seq

    def __len__(self):
        return len(self._sequence)

    def __getitem__(self, i: int):
        return self._sequence[i]

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            print(self[i], other[i])
            if self[i] != other[i]:
                return False
        return True


if __name__ == "__main__":
    mi_name = "eniitan"
    random_name = "kazeem"

    my_sequence = CustomSequence(mi_name)
    other_sequence = CustomSequence(random_name)
    print(my_sequence == other_sequence)
