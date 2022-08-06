# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/int10.cairo#L111

class Int:
    value: int  # felt


PRIME = 2**251 + 17 * 2**192 + 1


def hint(a: Int, b: Int, SHIFT: int = 2**9):
    # Let's figure out what a and b were as Python integers in [-SHIFT, SHIFT):
    a_value = a.value if a.value < SHIFT else a.value - PRIME
    b_value = b.value if b.value < SHIFT else b.value - PRIME
    # Multiply them
    m_value = a_value * b_value
    # Do the division
    (runner_overflow, runner_res) = divmod(m_value, 2 * SHIFT)
    # runner_res is nearly what we want ... but it's in [0, 2 * SHIFT) whereas we need something in [-SHIFT, SHIFT).
    if runner_res >= SHIFT:
        m_res = (runner_res - 2 * SHIFT) % PRIME
        m_overflow = (runner_overflow + 1) % PRIME
    else:
        m_res = runner_res
        m_overflow = runner_overflow % PRIME
    # Worked example:
    # Suppose SHIFT = 128 (so 8-bit integers) and m_value = -127.
    # Then divmod(-127, 256) = (-1, 129) and m_res = -127 and m_overflow = 0
    # Then divmod(-129, 256) = (-1, 127) and m_res = 127 and m_overflow = -1
