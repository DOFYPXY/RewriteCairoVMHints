# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo#L20

from typing import Union

PRIME = 2**251 + 17 * 2**192 + 1


class RelocatableValue:
    segment_index: int
    offset: int


def hint(a, b):
    both_ints = isinstance(a, int) and isinstance(b, int)
    both_relocatable = (
        isinstance(a, RelocatableValue) and isinstance(b, RelocatableValue) and
        a.segment_index == b.segment_index)
    assert both_ints or both_relocatable, f'assert_not_equal failed: non-comparable values: {a}, {b}.'
    if both_ints:
        assert (a - b) % PRIME != 0, f'assert_not_equal failed: {a} = {b}.'
    if both_relocatable:
        assert (
            a.offset - b.offset) % PRIME != 0, f'assert_not_equal failed: {a} = {b}.'
