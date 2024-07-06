# Exercise R-2.12 asks for an implementation of __mul__, for the Vector class of Section 2.3.3, to provide support for the syntax v 3. Implement the __rmul__ method, to provide additional support for syntax 3 * v.

from exercise6 import Vector


# extending so I don't keep copy pasting
class UpdatedVector(Vector):
    def __init__(self, d):
        super().__init__(d)

    def __rmul__(self, other):
        if type(other) != int:
            raise TypeError("multiplier must be an integer")

        result = Vector(len(self))

        for i in range(len(result)):
            result[i] = self[i] * other

        return result


if __name__ == "__main__":
    v = UpdatedVector(3)
    v[0], v[1], v[2] = 10, 20, 30

    print(3 * v)
