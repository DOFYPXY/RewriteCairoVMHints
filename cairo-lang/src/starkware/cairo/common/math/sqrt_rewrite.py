# source: https://github.com/starkware-libs/cairo-lang/blob/13cef109cd811474de114925ee61fd5ac84a25eb/src/starkware/cairo/common/math.cairo#L353

PRIME = 2**251 + 17 * 2**192 + 1


def isqrt(n: int) -> int:
    """
    Returns the integer square root of the nonnegative integer n. This is the floor of the exact
    square root of n.
    Unlike math.sqrt(), this function doesn't have rounding error issues.
    """
    assert n >= 0

    # The following algorithm was copied from
    # https://stackoverflow.com/questions/15390807/integer-square-root-in-python.
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    assert x**2 <= n < (x + 1) ** 2
    return x


def hint(value):
    value = value % PRIME
    assert value < 2 ** 250, f"value={value} is outside of the range [0, 2**250)."
    assert 2 ** 250 < PRIME
    root = isqrt(value)
