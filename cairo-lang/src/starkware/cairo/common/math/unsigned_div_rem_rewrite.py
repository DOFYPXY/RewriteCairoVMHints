# source: https://github.com/starkware-libs/cairo-lang/blob/13cef109cd811474de114925ee61fd5ac84a25eb/src/starkware/cairo/common/math.cairo#L266

class RangeCheckBuiltinRunner:
    bound: int


PRIME = 2**251 + 17 * 2**192 + 1


def assert_integer(val):
    """
    Asserts that the input is an integer (and not relocatable value).
    """
    assert isinstance(val, int), f"Expected integer, found: {val}."


def hint(value, div, range_check_builtin: RangeCheckBuiltinRunner):
    assert_integer(div)
    assert 0 < div <= PRIME // range_check_builtin.bound, \
        f'div={hex(div)} is out of the valid range.'
    q, r = divmod(value, div)
