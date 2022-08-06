def assert_integer(val):
    """
    Asserts that the input is an integer (and not relocatable value).
    """
    assert isinstance(val, int), f"Expected integer, found: {val}."


PRIME = 2**251 + 17 * 2**192 + 1


def hint(a, b):
    assert_integer(a)
    assert_integer(b)
    assert (a % PRIME) < (b % PRIME), \
        f'a = {a % PRIME} is not less than b = {b % PRIME}.'
