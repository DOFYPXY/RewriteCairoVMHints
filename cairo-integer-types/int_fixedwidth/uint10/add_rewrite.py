# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/uint10.cairo#L44

class Int:
    value: int  # felt


def hint(a: Int, b: Int, SHIFT: int = 2**10):
    res = Int()
    (carry, res.value) = divmod(a.value + b.value, SHIFT)
