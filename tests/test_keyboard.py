import pytest

from src.keyboard import Keyboard

@pytest.fixture
def test_example3():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    return keyboard


def test_class_item_init(test_example3):
    assert str(test_example3) == "Dark Project KD87A"
    assert str(test_example3.language) == "EN"


def test_change_lang(test_example3):
    test_example3.change_lang()
    assert str(test_example3.language) == "RU"
    test_example3.change_lang().change_lang()
    assert str(test_example3.language) == "RU"
