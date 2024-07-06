# At the close of Section 2.4.1, we suggest a model in which the CreditCard class supports a nonpublic method, _set_balance(b), that could be used by subclasses to affect a change to the balance, without directly accessing the balance data member. Implement such a model, revising both the CreditCard and PredatoryCreditCard classes accordingly.

import os, sys

grandparent_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../python_DSA")
)

sys.path.append(grandparent_folder)

from demo1_class import CreditCard


class CustomCreditCard(CreditCard):
    def __init__(
        self,
        customer: str,
        bank: str,
        account: str,
        limit: int,
        initial_balance=None,
    ):
        super().__init__(customer, bank, account, limit, initial_balance)

    def _set_balance(self, num: int):
        if isinstance(num, int):
            self._balance = num
        else:
            raise TypeError("parameter must be an integer")


class PredatoryCreditCard(CustomCreditCard):
    def __init__(
        self,
        customer: str,
        bank: str,
        account: str,
        limit: int,
        initial_balance=None,
    ):
        super().__init__(customer, bank, account, limit, initial_balance)

    OVERLIMIT_FEE = 5

    # overrides the charge method in the parent class
    def charge(self, price):
        # returns a boolean
        success = super().charge(price)

        if not success:
            current_balance = self.get_balance()
            self._set_balance(current_balance + PredatoryCreditCard.OVERLIMIT_FEE)

        return success

    def process_month(self):
        """Accesses monthly interest on outstanding balance"""

        if self._balance > 0:
            monthly_factor = (1 + self._apr) ** 1 / 12
            current_balance = self.get_balance()
            self._set_balance(current_balance * monthly_factor)


if __name__ == "__main__":
    some_account = PredatoryCreditCard("Lionel Messi", "First Bank", "1633513853", 3000)

    print(some_account.charge(5))
