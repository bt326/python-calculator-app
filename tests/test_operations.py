import pytest
from app.operations import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 2.5, 5.0),
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (1, 1, 0),
        (0, 5, -5),
    ]
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-2, 2, -4),
        (0, 5, 0),
    ]
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 2, 3),
        (5, 2, 2.5),
    ]
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
from app.repl import get_number


def test_get_number_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    result = get_number("Enter:")
    assert result == 5.0


def test_get_number_invalid_then_valid(monkeypatch):
    inputs = iter(["abc", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_number("Enter:")
    assert result == 3.0
