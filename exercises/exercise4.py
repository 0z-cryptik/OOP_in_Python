# Implement the __neg__ method for the Vector class of Section 2.3.3, so that the expression −v returns a new vector instance whose coordinates are all the negated values of the respective coordinates of v.


class Vector:
    def __init__(self, d):
        # initializes a list of d number of zeros
        self._coords = [0] * d

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

    def __neg__(self):
        result = Vector(len(self))

        for i in range(len(result)):
            result[i] = -1 * self[i]
        return result

    def __str__(self) -> str:
        # the [1: -1] is to remove the [] enclosing
        return "<" + str(self._coords)[1:-1] + ">"


if __name__ == "__main__":
    mi_vec = Vector(3)
    mi_vec[0] = 10
    mi_vec[1] = 20
    mi_vec[2] = 30

    print(-mi_vec)

    v = Vector(2)
    v[0], v[1] = 2, 4

    # u returns <12, 15>
    u = v + [10, 11]
    print(u)
