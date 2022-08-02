from starkware.cairo.common.math_utils import assert_integer
assert_integer(ids.a)
assert_integer(ids.b)
a = ids.a % PRIME
b = ids.b % PRIME
assert a <= b, f'a = {a} is not less than or equal to b = {b}.'

ids.small_inputs = int(
    a < range_check_builtin.bound and (b - a) < range_check_builtin.bound)
