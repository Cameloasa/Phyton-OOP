"""
Skapa en klass som representerar ett bankkonto. Banken ska kunna:
sätta in pengar (deposit)
ta up pengar (withdraw)
returnera nuvarande saldo (balance)
räkna ut ränta (apply_interest, lägger till räntan till kontot)
tala om ifall man har råd att betala en räkning (returnera True/False)

Gör en metod för varje funktion.

"""

class BankAccount:

    #constructor
    def __init__(self, balance=0):
        self.__balance = balance  # Privat variabel för saldo

    #returnera nuvarande saldo (balance)
    def show_balance(self):
        """Returnerar nuvarande saldo."""
        return self.__balance

    #sätta in pengar (deposit)
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Beloppet måste vara positiv.')
        self.__balance += amount

    #ta up pengar (withdraw)
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Beloppet måste vara positivt.')
        if amount > self.__balance:
            raise ValueError('Otillräckliga medel.')
        self.__balance -= amount

    #räkna ut ränta (apply_interest, lägger till räntan till kontot)
    def apply_interest(self, rate):
        if rate < 0:
            raise ValueError('Räntan måste vara positiv.')
        self.__balance += self.__balance * rate

    #tala om ifall man har råd att betala en räkning (returnera True/False)
    def can_pay(self, amount):
        return self.__balance >= amount


