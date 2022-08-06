# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/edf804eb00b585f3f20e22f8318b5297dc8a043f/int_fixedwidth/uint10.cairo#L60

class Int:
    value: int  # felt


def hint(a: Int, b: Int, SHIFT: int = 2**10):
    res = Int()
    (carry, res.value) = divmod(a.value - b.value, SHIFT)
    borrow = -carry  # if b > a then carry is -1
