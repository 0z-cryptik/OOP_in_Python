# Give a short fragment of Python code that uses the progression classes from Section 2.4.2 to find the 8th value of a Fibonacci progression that starts with 2 and 2 as its first two values.

import sys, os, random

grandparent_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../python_DSA")
)
sys.path.append(grandparent_folder)

from demo7_progression import FibonacciProgression


class MyFiboClass(FibonacciProgression):
    def __init__(self, first=0, second=1) -> None:
        super().__init__(first, second)

    def return_progression(self, n: int):
        return [next(self) for i in range(n)]


if __name__ == "__main__":
    def return_8th_num():
        rn1 = random.randint(1, 10)
        rn2 = random.randint(1, 10)
        random_fibo_sequence = MyFiboClass(rn1, rn2)
        first_8_numbers = random_fibo_sequence.return_progression(8)

        if first_8_numbers[0] == 2 and first_8_numbers[1] == 2:
            return first_8_numbers[7]
        else:
            return "nope"

    print(return_8th_num())
