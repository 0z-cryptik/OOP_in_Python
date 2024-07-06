# The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to 0. Another convenient form for creating a new vector would be to send the constructor a parameter that is some iterable type representing a sequence of numbers, and to create a vector with dimension equal to the length of that sequence and coordinates equal to the sequence values. For example, Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these forms is acceptable; that is, if a single integer is sent, it produces a vector of that dimension with all zeros, but if a sequence of numbers is provided, it pro- duces a vector with coordinates based on that sequence.


class Vector:
    def __init__(self, d):
        if isinstance(d, list) or isinstance(d, tuple) or isinstance(d, set):
            self._coords = [val for val in d if type(val) == int]
        elif type(d) == int:
            self._coords = [0] * d
        else:
            raise TypeError("argument must be an iterable of integers or an integer")

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, i):
        return self._coords[i]

    def __setitem__(self, i, new_value):
        self._coords[i] = new_value

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self._coords == other._coords

    def __add__(self, other):
        # len(self) call the __len__ method defined earlier, so it returns the length of self._coords as defined in the __len__ method
        if len(self) != len(other):
            raise ValueError("The lengths must be the same")

        result = Vector(len(self))

        for i in range(len(result)):
            result[i] = other[i] + self[i]
        return result

    def __mul__(self, other):
        if type(other) != int:
            raise TypeError("multiplier must be an integer")

        result = Vector(len(self))

        for i in range(len(result)):
            result[i] = self[i] * other

        return result

    def __str__(self) -> str:
        # the [1: -1] is to remove the [] enclosing
        return "<" + str(self._coords)[1:-1] + ">"


if __name__ == "__main__":
    list_int = [1, 2, 3]
    set_int = {4, 5, 6}
    tuple_int = (7, 8)

    v = Vector(list_int)
    u = Vector(3)
    y = Vector(set_int)
    z = Vector(tuple_int)

    print(v, u, y, z)
