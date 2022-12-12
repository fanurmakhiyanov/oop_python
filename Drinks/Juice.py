from Drinks import Drink


# Создаём класс-потомок и указываем в скобках родительский класс, от которого наследуем.
class Juice(Drink):
    # Вызываем инициализатор класса и указываем в нём новый динамический атрибут taste.
    def __init__(self, name, price, taste):
        # Вызываем конструктор класса-родителя и просим его определить значения динамических атрибутов, которые в нём
        # прописаны.
        super().__init__(name, price)
        # Определяем значение нового динамического атрибута taste.
        self.taste = taste


# Создаём экземпляр класса Juice.
apple_juice = Juice('Сок', 250, 'яблочный')

# Пробуем вызвать методы, прописанные в родительском классе Drink.
apple_juice.small_sip()  # Говорим другу сделать маленький глоток.
apple_juice.sip()  # Говорим другу сделать обычный глоток.
apple_juice.drink_info()  # Просим друга сообщить информацию о напитке.
