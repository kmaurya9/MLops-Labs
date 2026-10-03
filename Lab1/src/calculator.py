"""Basic arithmetic functions used in MLOps Lab 1."""

Number = (int, float)


def _validate(*values):
    """Raise ValueError if any value is not an int or float (bools are rejected)."""
    for value in values:
        if isinstance(value, bool) or not isinstance(value, Number):
            raise ValueError(f"Expected a number, got {type(value).__name__}: {value!r}")


def fun1(x, y):
    """Return the sum of x and y."""
    _validate(x, y)
    return x + y


def fun2(x, y):
    """Return x minus y."""
    _validate(x, y)
    return x - y


def fun3(x, y):
    """Return the product of x and y."""
    _validate(x, y)
    return x * y


def fun4(x, y):
    """Combine fun1, fun2 and fun3 on (x, y) and return the sum of their results."""
    return fun1(x, y) + fun2(x, y) + fun3(x, y)


def fun5(x, y):
    """Return x divided by y. Raises ZeroDivisionError when y is 0."""
    _validate(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


if __name__ == "__main__":
    print(fun4(2, 3))
