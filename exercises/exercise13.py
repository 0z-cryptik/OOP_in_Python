# ExerciseR-2.12 uses the __mul__ method to support multiplying a Vector by a number, while Exercise R-2.14 uses the __mul__ method to support computing a dot product of two vectors. Give a single implementation of Vector. __mul__ that uses run-time type checking to support both syntaxes u * v and u * k, where u and v designate vector instances and k represents a number.

from exercise3 import Vector


class CustomVector(Vector):
    def __init__(self, d: int):
        super().__init__(d)

    def __mul__(self, other: int | Vector):
        if isinstance(other, int):
            result = Vector(len(self))

            for i in range(len(result)):
                result[i] = self[i] * other

            return result

        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("The lengths must be the same")

            result = 0

            for i in range(len(self)):
                result += self[i] * other[i]

            return result


if __name__ == "__main__":
    v = CustomVector(3)
    v[0], v[1], v[2] = 10, 20, 30

    u = CustomVector(3)
    u[0], u[1], u[2] = 11, 21, 31

    print(v * 3)
    print(v * u)

    # to confirm the answer
    print((10 * 11) + (20 * 21) + (30 * 31))
