# The PredatoryCreditCard class of Section 2.4.1 provides a process_month method that models the completion of a monthly cycle. Modify the class so that once a customer has made ten calls to charge in the current month, each additional call to that function results in an additional $1 surcharge.

import os, sys

grandparent_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../python_DSA")
)

sys.path.append(grandparent_folder)

from demo6_inheritance import PredatoryCreditCard


class CustomPredatoryCreditCard(PredatoryCreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit, apr)

    def charge(self, price):
        times = 0
        times += 1

        if times >= 10:
            price = price + 1

        # returns a boolean
        success = super().charge(price)

        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE

        return success


mi_credit_card = CustomPredatoryCreditCard(
    "Lebron James", "GTB", "13325526", 2500, 0.09
)

print(mi_credit_card.charge(20))
