from demo1_class import CreditCard

# extends class CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    __slots__ = "_apr"
    OVERLIMIT_FEE = 5

    # overrides the charge method in the parent class
    def charge(self, price):
        # returns a boolean
        success = super().charge(price)

        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE

        return success

    def process_month(self):
        """Accesses monthly interest on outstanding balance"""

        if self._balance > 0:
            monthly_factor = (1 + self._apr) ** 1 / 12
            self._balance *= monthly_factor
