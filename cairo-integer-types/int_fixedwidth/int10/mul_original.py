# https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/int10.cairo#L111

# Let's figure out what a and b were as Python integers in [-SHIFT, SHIFT):
a_value = ids.a.value if ids.a.value < ids.SHIFT else ids.a.value - PRIME
b_value = ids.b.value if ids.b.value < ids.SHIFT else ids.b.value - PRIME
# Multiply them
m_value = a_value * b_value
# Do the division
(runner_overflow, runner_res) = divmod(m_value, 2 * ids.SHIFT)
# runner_res is nearly what we want ... but it's in [0, 2 * SHIFT) whereas we need something in [-SHIFT, SHIFT).
if runner_res >= ids.SHIFT:
    ids.m_res = (runner_res - 2 * ids.SHIFT) % PRIME
    ids.m_overflow = (runner_overflow + 1) % PRIME
else:
    ids.m_res = runner_res
    ids.m_overflow = runner_overflow % PRIME
# Worked example:
# Suppose SHIFT = 128 (so 8-bit integers) and m_value = -127.
# Then divmod(-127, 256) = (-1, 129) and m_res = -127 and m_overflow = 0
# Then divmod(-129, 256) = (-1, 127) and m_res = 127 and m_overflow = -1
