"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
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