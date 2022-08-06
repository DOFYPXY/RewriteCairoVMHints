from starkware.cairo.common.math_utils import assert_integer
assert_integer(ids.a)
assert 0 <= ids.a % PRIME < range_check_builtin.bound, f'a = {ids.a} is out of range.'
