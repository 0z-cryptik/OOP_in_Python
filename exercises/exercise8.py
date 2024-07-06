# Implement the __mul__ method for the Vector class of Section 2.3.3, so that the expression u * v returns a scalar that represents the dot product of the vectors, that is, ∑di=1 ui · vi

from exercise3 import Vector


class UpdatedVector(Vector):
    def __init__(self, d):
        super().__init__(d)

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("The lengths must be the same")

        result = 0

        for i in range(len(self)):
            result += self[i] * other[i]

        return result


if __name__ == "__main__":
    v = UpdatedVector(2)
    v[0], v[1] = 2, 4

    u = UpdatedVector(2)
    u[0], u[1] = 5, 6

    print(v * u)
