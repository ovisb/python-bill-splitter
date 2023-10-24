import io

import pytest

from python_bill_splitter.python_bill_splitter import (
    create_friends_dict,
    get_number_of_friends,
)


def test_number_of_friends(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("5\n"))
    assert get_number_of_friends() == 5


def test_raise_value_error_number_of_friends(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("asd\n"))
    with pytest.raises(ValueError):
        assert get_number_of_friends()


def test_create_friends_dict(monkeypatch):
    inputs = "Marc\nJem\nMonica\nAnna\nJason\n"
    expected = {"Marc": 0, "Jem": 0, "Monica": 0, "Anna": 0, "Jason": 0}
    friends_number = 5
    monkeypatch.setattr("sys.stdin", io.StringIO(inputs))
    assert create_friends_dict(friends_number) == expected


def test_negative_create_friends_dict(monkeypatch):
    inputs = "Marc\nJem\nMonica\nAnna\nJason\n"
    friends_number = -1
    monkeypatch.setattr("sys.stdin", io.StringIO(inputs))
    assert create_friends_dict(friends_number) == {}
