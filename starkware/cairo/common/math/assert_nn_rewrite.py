# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo#L40

class RangeCheckBuiltinRunner:
    bound: int


def assert_integer(val):
    """
    Asserts that the input is an integer (and not relocatable value).
    """
    assert isinstance(val, int), f"Expected integer, found: {val}."


PRIME = 2**251 + 17 * 2**192 + 1


def hint(a, range_check_builtin: RangeCheckBuiltinRunner):
    assert_integer(a)
    assert 0 <= a % PRIME < range_check_builtin.bound, f'a = {a} is out of range.'
