# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo#L237

class RangeCheckBuiltinRunner:
    bound: int


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


def is_positive(value, prime, rc_bound):
    """
    Returns True if the lift of the given field element, as an integer in the range
    (-rc_bound, rc_bound), is positive.
    Raises an exception if the element is not within that range.
    """
    val = as_int(value, prime)
    assert abs(val) < rc_bound, f"value={val} is out of the valid range."
    return val > 0


PRIME = 2**251 + 17 * 2**192 + 1


def hint(value, range_check_builtin: RangeCheckBuiltinRunner):
    is_positive = 1 if is_positive(
        value=value, prime=PRIME, rc_bound=range_check_builtin.bound) else 0
