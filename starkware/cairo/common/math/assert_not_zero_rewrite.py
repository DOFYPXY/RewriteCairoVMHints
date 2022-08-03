# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo#L5

PRIME = 2**251 + 17 * 2**192 + 1


def assert_integer(val):
    """
    Asserts that the input is an integer (and not relocatable value).
    """
    assert isinstance(val, int), f"Expected integer, found: {val}."


def hint(value):
    assert_integer(value)
    assert value % PRIME != 0, f'assert_not_zero failed: {value} = 0.'
