def square(x: int | float) -> int | float:
    """Return the square of the number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the number raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Run arg function in a closure and return the inner function."""
    count = 0
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    count = x
    return inner
