import Drinks


class Drink:
    _volume = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._remains = self._volume

    def drink_info(self):
        print(
            f'Название: {self.name}\nСтоимость: {self.price} руб.\nНачальный объем: {self._volume} мл.\nОсталось: {self._remains} мл.')

    # Служебный метод, чтобы узнать, достаточно ли напитка.
    def _is_enough(self, need):
        if self._remains >= need and self.remains > 0:
            return True
        print('Осталось недостаточно напитка')
        return False

    # Говорим другу сделать глоток.
    def sip(self):
        if self._is_enough(20):
            self._remains -= 20
            print('Друг сделал глоток')

    # Говорим другу сделать маленький глоток.
    def small_sip(self):
        if self._is_enough(10):
            self._remains -= 10
            print('Друг сделал маленький глоток')

    # Говорим другу выпить напиток залпом.
    def drink_all(self):
        if self._is_enough(0):
            self._remains = 0
            print('Друг выпил напиток залпом')


coffee = Drink('Капуччино', 300)  # Заказываем кофе.
coffee._remains = 10  # Приравниваем остаток кофе к 10 мл.
coffee.sip()  # Пытаемся сделать обычный глоток.
coffee.drink_info()  # Узнаём информацию о напитке.
