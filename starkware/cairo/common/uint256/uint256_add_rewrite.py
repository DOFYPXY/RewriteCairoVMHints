# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/uint256.cairo#L36

class Uint256:
    low: int  # felt
    high: int  # felt


def hint(a: Uint256, b: Uint256, SHIFT: int = 2**128):
    sum_low = a.low + b.low
    carry_low = 1 if sum_low >= SHIFT else 0
    sum_high = a.high + b.high + carry_low
    carry_high = 1 if sum_high >= SHIFT else 0
