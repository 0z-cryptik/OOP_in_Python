class Progression:
    """
    Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0) -> None:
        self._current = start

    __slots__ = "_current"

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            # returns current value then increases it, so it returns an incremented one next time. Hence 0, 1, 2...
            currentValue = self._current
            self._advance()
            return currentValue

    def __iter__(self):
        return self

    def print_progression(self, n):
        """Print the next n values of the progression"""
        # this calls to the __next__ method declared earlier
        print(", ".join(str(next(self)) for j in range(n)))


class ArithmethicProgression(Progression):
    def __init__(self, increment, start=0) -> None:
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):
    # start cannot be 0 in a geometric progression
    def __init__(self, base, start=1) -> None:
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1) -> None:
        super().__init__(first)
        # initial prev, will be reassigned to current value in the advance method
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, (self._prev + self._current)


if __name__ == "__main__":
    mi_progression = Progression(1)
    print("Default Progression:")
    mi_progression.print_progression(10)

    mi_arr_progression = ArithmethicProgression(2, 2)
    print("Arithmethic Progression:")
    mi_arr_progression.print_progression(12)

    mi_geo_progression = GeometricProgression(2)
    print("Geometric Progression:")
    mi_geo_progression.print_progression(7)

    mi_fib_progression = FibonacciProgression()
    print("Fibonacci Progression:")
    mi_fib_progression.print_progression(10)
