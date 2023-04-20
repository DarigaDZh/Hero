class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму, которую вы хотите добавить: "))
        self.__balance += amount
        print("Ваш новый баланс: ", self.__balance)

    def __kill(self):
        self.__balance = 0
        print("Все деньги с вашего счета были обнулены.")

    def _jackpot(self):
        self.__balance *= 10
        print("Вы выиграли джекпот! Ваш новый баланс: ", self.__balance)

    def _merge_balance(self, other):
        other_balance = other.get_balance()
        self.__balance += other_balance
        other.__kill()
        print(f"Баланс {self.__name}: {self.__balance}")

    def get_balance(self):
        return self.__balance


# Создаем два объекта
client1 = Bank("Клиент 1", 100)
client2 = Bank("Клиент 2", 100)

# Проверяем работу методов
client1.moneyX()  # добавляем деньги на счет
client1._jackpot()  # выигрываем джекпот
client2._merge_balance(client1)  # объединяем балансы клиентов


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y


# Создаем два объекта
num1 = Calculator(10, 20)
num2 = Calculator(5, 10)

# Проверяем работу методов
print(num1 + num2)  # сложение
print(num1 - num2)  # вычитание
print(num1 * num2)  # умножение
print(num1 / num2)  # деление
