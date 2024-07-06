# Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type.


class Flower:
    def __init__(
        self,
        name: str,
        num_of_petals: int,
        price: float,
    ) -> None:
        if type(name) != str or type(num_of_petals) != int or type(price) != float:
            raise TypeError(
                "Instance variables do not follow the the right type annotations"
            )
        self._name = name
        self._num_of_petals = num_of_petals
        self._price = price

    def get_name(self):
        return self._name

    def get_num_of_petals(self):
        return self._num_of_petals

    def get_price(self):
        return self._price

    def set_new_name(self, new_name: str) -> None:
        if type(new_name) != str:
            raise TypeError("Name must be string")
        self._name = new_name

    def set_new_num_of_petals(self, val: int) -> None:
        if type(val) != int:
            raise TypeError("Value must be an integer")
        self._num_of_petals = val

    def set_new_price(self, val: float) -> None:
        if type(val) != float:
            raise TypeError("Value must be a float")
        self._price = val


if __name__ == "__main__":
    harbiscus = Flower("Harbiscus", 5, 20.0)
    harbiscus.set_new_name('Rose')
    print(harbiscus.get_name())
