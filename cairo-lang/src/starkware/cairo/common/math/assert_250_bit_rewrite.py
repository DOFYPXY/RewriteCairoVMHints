# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo#L95

def assert_integer(val):
    """
    Asserts that the input is an integer (and not relocatable value).
    """
    assert isinstance(val, int), f"Expected integer, found: {val}."


def as_int(val, prime):
    """
    Returns the lift of the given field element, val, as an integer in the range
    (-prime/2, prime/2).
    """
    assert_integer(val)
    return val if val < prime // 2 else val - prime


PRIME = 2**251 + 17 * 2**192 + 1


def hint(value, UPPER_BOUND: int = 2**250, SHIFT: int = 2**128):
    # Correctness check.
    value = as_int(value, PRIME) % PRIME
    assert value < UPPER_BOUND, f'{value} is outside of the range [0, 2**250).'

    # Calculation for the assertion.
    high, low = divmod(value, SHIFT)
