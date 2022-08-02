from starkware.cairo.common.math_utils import assert_integer
assert_integer(ids.value)
assert ids.value % PRIME != 0, f'assert_not_zero failed: {ids.value} = 0.'
