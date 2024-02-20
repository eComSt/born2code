class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __repr__(self):
        return f"BankAccount({self.__balance})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return BankAccount(self.__balance + other)
        else:
            print("Некорректное пополнение счета")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            if self.__balance >= other:
                return BankAccount(self.__balance - other)
            else:
                print("Баланс не может стать отрицательным!")
        else:
            print("Некорректное списание средств со счета")

a = BankAccount(100)
a = a + 150
print(a)