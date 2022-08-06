# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/int10.cairo#L163
class Int:
    value: int  # felt


def hint(a_abs: int, b_abs: int):
    quotient = Int()
    remainder = Int()
    quotient.value, remainder.value = divmod(a_abs, b_abs)
