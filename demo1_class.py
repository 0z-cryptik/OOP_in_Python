class CreditCard:
    def __init__(
        self,
        customer,
        bank,
        account,
        limit,
        initial_balance=None,
    ):
        """creates a new credit card instance"""
        # like a constructor in javascript

        self._customer = customer
        self._account = account
        self._bank = bank
        self._limit = limit
        if initial_balance != None:
            if type(initial_balance) != int:
                raise TypeError("Value must be an integer")
            self._balance = initial_balance
        else:
            self._balance = 0

    # to avoid instance dicts
    __slots__ = (
        "_customer",
        "_account",
        "_bank",
        "_limit",
        "_balance",
    )

    def get_customer(self):
        """returns the name of the customer"""
        return self._customer

    def get_account(self):
        """returns the card identifying number (typically stored as a string)"""
        return self._account

    def get_bank(self):
        """returns the banks name"""
        return self._bank

    def get_limit(self):
        """returns the current credit card limit"""
        return self._limit

    def get_balance(self):
        """returns the current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied."""

        if type(price) != int:
            raise TypeError("Value must be a number")

        if price + self._balance > self._limit:
            # reject charge if it would exceed limit
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        if type(amount) != int:
            raise TypeError("Value must be a number")
        elif amount < 0:
            raise ValueError("Value must be a positive number")
        self._balance -= amount


# won't run when something is exported from this file
if __name__ == "__main__":
    wallet = []
    wallet.append(
        CreditCard(
            customer="Joseph Yobo", bank="Union Bank", account="29346576289", limit=2500
        )
    )
    wallet.append(
        CreditCard(
            customer="Jay Jay Okocha",
            bank="Bank of England",
            account="2211-333-444",
            limit=3500,
        )
    )
    wallet.append(
        CreditCard(
            customer="Mario Balotelli",
            bank="Bank of Italy",
            account="6538793793",
            limit=5000,
        )
    )

    for i in range(1, 17):
        wallet[0].charge(500 * i)
        wallet[1].charge(2 * i)
        wallet[2].charge(3 * i)

    for j in range(3):
        print("Customer:", wallet[j].get_customer())
        print("Bank:", wallet[j].get_bank())
        print("Account ID:", wallet[j].get_account())
        print("Limit:", wallet[j].get_limit())
        print("Balance:", wallet[j].get_balance())

        while wallet[j].get_balance() > 100:
            wallet[j].make_payment(100)
            print("New balance:", wallet[j].get_balance())
