# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo#L132

PRIME = 2**251 + 17 * 2**192 + 1


def assert_integer(val):
    """
    Asserts that the input is an integer (and not relocatable value).
    """
    assert isinstance(val, int), f"Expected integer, found: {val}."


def hint(value, MAX_HIGH: int = (-1) / 2 ** 128, MAX_LOW=0):
    assert MAX_HIGH < 2**128 and MAX_LOW < 2**128
    assert PRIME - 1 == MAX_HIGH * 2**128 + MAX_LOW
    assert_integer(value)
    low = value & ((1 << 128) - 1)
    high = value >> 128
