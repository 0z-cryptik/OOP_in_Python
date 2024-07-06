# In similar spirit to the previous problem, augment the Sequence class with method __lt__, to support lexicographic comparison seq1 < seq2.

from exercise11 import CustomSequence


class ExtendedCustomSequence(CustomSequence):
    def __init__(self, seq) -> None:
        super().__init__(seq)

    def __lt__(self, other):
        return self._sequence < other._sequence


seq1 = "DATA"
seq2 = "data"

primary_sequence = ExtendedCustomSequence(seq1)
secondary_sequence = ExtendedCustomSequence(seq2)

print(primary_sequence < secondary_sequence)
