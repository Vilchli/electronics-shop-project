import csv
import os
from pathlib import Path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

         Название товара.
         Цена за единицу товара.
         Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        path = Path('C:\Users\Vil\electronics-shop-project\src\items.csv').resolve()
        with open(path, encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=" ")
            for item in reader:
                cls.all.append(cls(item['name'], int(item['price']), int(item['quantity'])))

    @staticmethod
    def string_to_number(item):
        return int(float(item))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
