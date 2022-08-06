from starkware.cairo.common.math_utils import as_int, assert_integer

assert_integer(ids.div)
assert 0 < ids.div <= PRIME // range_check_builtin.bound, \
    f'div={hex(ids.div)} is out of the valid range.'

assert_integer(ids.bound)
assert ids.bound <= range_check_builtin.bound // 2, \
    f'bound={hex(ids.bound)} is out of the valid range.'

int_value = as_int(ids.value, PRIME)
q, ids.r = divmod(int_value, ids.div)

assert -ids.bound <= q < ids.bound, \
    f'{int_value} / {ids.div} = {q} is out of the range [{-ids.bound}, {ids.bound}).'

ids.biased_q = q + ids.bound
