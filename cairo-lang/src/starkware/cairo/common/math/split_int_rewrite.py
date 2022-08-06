# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/math.cairo#L335

from typing import List


class RelocatableValue:
    segment_index: int
    offset: int


PRIME = 2**251 + 17 * 2**192 + 1


def hint(value, base, bound, memory: List[List[int]], output: RelocatableValue):
    memory[output.segment_index][output.offset] = res = (
        int(value) % PRIME) % base
    assert res < bound, f'split_int(): Limb {res} is out of range.'
