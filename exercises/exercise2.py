# The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a nonzero balance using an optional fifth parameter to the constructor. The four-parameter constructor syntax should continue to produce an account with zero balance.


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
