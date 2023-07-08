"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item

from src.phone import Phone

def test_class_item(test_example):
    assert test_example.name == "Смартфон"
    assert test_example.price == 10000
    assert test_example.quantity == 20
    assert test_example.calculate_total_price() == 200000
    test_example.apply_discount()
    assert test_example.price == 8000


@pytest.fixture
def test_example():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    return item1


def test_repr_str(test_example):
    assert repr(test_example) == "Item('Смартфон', 10000, 20)"
    assert str(test_example) == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('2.0') == 2
    assert Item.string_to_number('2.4') == 2


def test_name_setter(test_example):
    test_example.name = "Телефон"
    assert test_example.name == "Телефон"
    test_example.name = "Новый Телефон"
    assert test_example.name == "Новый Теле"



