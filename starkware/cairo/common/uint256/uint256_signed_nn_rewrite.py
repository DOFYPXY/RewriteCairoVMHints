# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/uint256.cairo#L161

from typing import List


class Uint256:
    low: int  # felt
    high: int  # felt


class RelocatableValue:
    segment_index: int
    offset: int


PRIME = 2**251 + 17 * 2**192 + 1


def hint(a: Uint256, memory: List[List[int]], ap: RelocatableValue):
    memory[ap.segment_index][ap.offset] = 1 if 0 <= (
        a.high % PRIME) < 2 ** 127 else 0
