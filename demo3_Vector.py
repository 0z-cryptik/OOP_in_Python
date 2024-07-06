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

    def __str__(self) -> str:
        # the [1: -1] is to remove the [] enclosing
        return "<" + str(self._coords)[1:-1] + ">"


mi_vector, mi_vector2 = Vector(5), Vector(5)
mi_vector[3] = 12
mi_vector[0] = 2
mi_vector[2] = 7

mi_vector2[3] = 2
mi_vector2[0] = 2
mi_vector2[2] = 2
print(mi_vector + mi_vector2)
