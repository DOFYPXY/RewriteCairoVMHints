# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/int10.cairo#L86

class Int:
    value: int  # felt


PRIME = 2**251 + 17 * 2**192 + 1


def hint(a: Int, b: Int, SHIFT: int = 2**9):
    res = Int()
    a_sub_b = (a.value - b.value) % PRIME
    if (a_sub_b >= SHIFT) and (a_sub_b < 2*SHIFT):
        (overflow, res.value) = (1, (a_sub_b - 2 * SHIFT) % PRIME)
    elif (a_sub_b < PRIME - SHIFT) and (PRIME - 2 * SHIFT <= a_sub_b):
        (overflow, res.value) = (-1 %
                                 PRIME, (a_sub_b + 2 * SHIFT) % PRIME)
    else:
        (overflow, res.value) = (0, a_sub_b)
