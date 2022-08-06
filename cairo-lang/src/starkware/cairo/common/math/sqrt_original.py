from starkware.python.math_utils import isqrt
value = ids.value % PRIME
assert value < 2 ** 250, f"value={value} is outside of the range [0, 2**250)."
assert 2 ** 250 < PRIME
ids.root = isqrt(value)
