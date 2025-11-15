class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def customer_name(self):
        return self._customer_name

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount
        return self._balance

    def __str__(self):
        return f"Account({self._account_number}) | Name: {self._customer_name} | Balance: {self._balance}"


class SavingsAccount(BankAccount):
    """Derived class showing inheritance"""

    def __init__(self, account_number, customer_name, balance=0, interest_rate=0.03):
        super().__init__(account_number, customer_name, balance)
        self._interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        return self._balance
