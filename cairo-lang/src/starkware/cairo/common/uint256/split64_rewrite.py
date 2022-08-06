# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/uint256.cairo#L59

def hint(a: int):
    low = a & ((1 << 64) - 1)
    high = a >> 64
