from starkware.cairo.common.math_utils import as_int

# Correctness check.
value = as_int(ids.value, PRIME) % PRIME
assert value < ids.UPPER_BOUND, f'{value} is outside of the range [0, 2**250).'

# Calculation for the assertion.
ids.high, ids.low = divmod(ids.value, ids.SHIFT)
