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
    def balance(self):
        """Returnerar nuvarande saldo."""
        return self.__balance



    #sätta in pengar (deposit)
    def deposit(self):

        pass

    #ta up pengar (withdraw)
    def withdraw(self):
        pass

    #räkna ut ränta (apply_interest, lägger till räntan till kontot)
    def apply_interest(self):
        pass

    #tala om ifall man har råd att betala en räkning (returnera True/False)
    def can_pay(self):
        pass


