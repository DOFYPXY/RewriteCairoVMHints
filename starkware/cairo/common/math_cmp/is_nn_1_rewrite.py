# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math_cmp.cairo#L24

from typing import List


class RelocatableValue:
    segment_index: int
    offset: int


class RangeCheckBuiltinRunner:
    bound: int


PRIME = 2**251 + 17 * 2**192 + 1


def hint(a, memory: List[List[int]], ap: RelocatableValue, range_check_builtin: RangeCheckBuiltinRunner):
    memory[ap.segment_index][ap.offset] = 0 if 0 <= (
        (-a-1) % PRIME) < range_check_builtin.bound else 1
