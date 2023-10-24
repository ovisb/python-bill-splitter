import io

import pytest

from python_bill_splitter.python_bill_splitter import (
    calculate_bill,
    create_friends_dict,
    get_number_of_friends,
    get_random_name,
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


def test_calculate_bill_even(monkeypatch):
    friends = {"Marc": 0, "Jem": 0, "Monica": 0, "Anna": 0, "Jason": 0}
    expected = {"Marc": 20, "Jem": 20, "Monica": 20, "Anna": 20, "Jason": 20}
    monkeypatch.setattr("sys.stdin", io.StringIO("100\n"))
    calculate_bill(friends)
    assert friends == expected


def test_calculate_bill_rounded(monkeypatch):
    friends = {
        "Marc": 0,
        "Jem": 0,
        "Monica": 0,
        "Anna": 0,
        "Jason": 0,
        "Ben": 0,
        "Ned": 0,
    }
    expected = {
        "Marc": 5.86,
        "Jem": 5.86,
        "Monica": 5.86,
        "Anna": 5.86,
        "Jason": 5.86,
        "Ben": 5.86,
        "Ned": 5.86,
    }
    monkeypatch.setattr("sys.stdin", io.StringIO("41\n"))
    calculate_bill(friends)
    assert friends == expected


def test_get_random_name():
    friends = {"Marc": 20, "Jem": 20, "Monica": 20, "Anna": 20, "Jason": 20}
    assert get_random_name(friends) in friends
