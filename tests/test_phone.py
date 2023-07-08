"""Здесь тесты с использованием pytest для модуля phone."""

import pytest

from src.phone import Phone


def test_class_item_init(test_example2):
    assert test_example2.name == "iPhone 14"
    assert test_example2.price == 120000
    assert test_example2.quantity == 5
    assert test_example2.number_of_sim == 2


def test_repr_str(test_example2):
    assert repr(test_example2) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(test_example2) == 'iPhone 14'


def test_number_of_sim(test_example2):
    test_example2.number_of_sim = 1
    assert test_example2.number_of_sim == 1


@pytest.fixture
def test_example2():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1
