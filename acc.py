class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def update(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# account=Account("balance.txt")
# print(account.balance)
# # account.deposit(8000)
# # account.update()
# print(account.balance)

# Here I am using inheretence to create a child class of a Chequeing account.
class Chequeing(Account):
    """This line would be used as a doc string to explain what this class does. In this case, it would describe a chequeing account."""
    # class variable
    type="Chequeing"

    # This __init__ funciton is the constructor
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance-amount-self.fee

# the line below this one is an instantiaion of a class I.E making an instance of the class Chequeing.
berts_chequeing=Chequeing("bert.txt", 1)
berts_chequeing.deposit(420)
berts_chequeing.transfer(69)
berts_chequeing.update()
print("Bert's Balance: " + str(berts_chequeing.balance))
print(berts_chequeing.type)
print(berts_chequeing.__doc__)

ernie_chequeing=Chequeing("ernie.txt", 1)
ernie_chequeing.deposit(420)
ernie_chequeing.transfer(69)
ernie_chequeing.update()
print("Erine's Balance: " + str(ernie_chequeing.balance))
print(ernie_chequeing.type)
