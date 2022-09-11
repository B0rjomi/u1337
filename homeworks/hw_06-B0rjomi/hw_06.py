class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self): #what about to try writing test comments?

        if self.value == 0:
            a = Fib(1)
        else:
            a = Fib(self.value + self.prev)
        a.prev = self.value
        return a

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.balance = 0
        self.stock = 0

    def vend(self):
        if self.stock == 0:
            return 'Товара нет в наличии.'
        if self.balance < self.price:
            balance_alert = self.price - self.balance
            return 'Нужно дополнительно внести {0} ₽.'.format(balance_alert)
        if self.balance > self.price:
            balance_alert = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return 'Получите {0} и сдачу {1} ₽.'.format(self.name, balance_alert)
        else:
            self.balance = 0
            self.stock -= 1
            return 'Получите {0}.'.format(self.name)


    def restock(self, num):
        self.stock += num
        print(f"'Количество товара «{self.name}»: {self.stock}'") #f-строка используется вместо .format

    def deposit(self,cash):
        if self.stock == 0:
            return 'Товара нет в наличии. Вот твои деньги — {0} ₽.'.format(cash)
        else:
            self.balance += cash #test comment
            return 'Доступно: {0} ₽'.format(self.balance)
