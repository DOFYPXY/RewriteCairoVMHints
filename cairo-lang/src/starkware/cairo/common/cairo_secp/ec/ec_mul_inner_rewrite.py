# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/cairo_secp/ec.cairo#L290

from typing import List


class RelocatableValue:
    segment_index: int
    offset: int


PRIME = 2**251 + 17 * 2**192 + 1


def hint(memory: List[List[int]], ap: RelocatableValue, scalar: int):
    memory[ap] = (scalar % PRIME) % 2
