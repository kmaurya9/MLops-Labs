import pytest

from src import calculator


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (5, 0, 5),
    (-1, 1, 0),
    (-1, -1, -2),
    (0.5, 0.25, 0.75),
])
def test_fun1(x, y, expected):
    assert calculator.fun1(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, -1),
    (5, 0, 5),
    (-1, 1, -2),
    (-1, -1, 0),
])
def test_fun2(x, y, expected):
    assert calculator.fun2(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-1, 1, -1),
    (-1, -1, 1),
])
def test_fun3(x, y, expected):
    assert calculator.fun3(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 10),    # 5 + (-1) + 6
    (5, 5, 35),    # 10 + 0 + 25
    (0, 0, 0),
    (-2, 4, -12),  # 2 + (-6) + (-8)
])
def test_fun4(x, y, expected):
    assert calculator.fun4(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (6, 3, 2),
    (1, 4, 0.25),
    (-9, 3, -3),
])
def test_fun5(x, y, expected):
    assert calculator.fun5(x, y) == pytest.approx(expected)


def test_fun5_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(1, 0)


@pytest.mark.parametrize("func", [
    calculator.fun1, calculator.fun2, calculator.fun3, calculator.fun4, calculator.fun5,
])
@pytest.mark.parametrize("bad_input", ["2", None, [1], True])
def test_invalid_inputs_raise(func, bad_input):
    with pytest.raises(ValueError):
        func(bad_input, 1)
