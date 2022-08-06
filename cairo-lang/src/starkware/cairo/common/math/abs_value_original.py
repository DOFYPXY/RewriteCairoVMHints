from starkware.cairo.common.math_utils import is_positive
ids.is_positive = 1 if is_positive(
    value=ids.value, prime=PRIME, rc_bound=range_check_builtin.bound) else 0
