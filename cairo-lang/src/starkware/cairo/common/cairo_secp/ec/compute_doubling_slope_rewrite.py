# https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/cairo_secp/ec.cairo#L57

from starkware.python.math_utils import ec_double_slope
from starkware.cairo.common.cairo_secp.secp_utils import SECP_P, pack

BASE = 2**86
SECP_P = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
PRIME = 2**251 + 17 * 2**192 + 1


class BigInt3:
    d0: int  # felt
    d1: int  # felt
    d2: int  # felt


class EcPoint:
    x: BigInt3
    y: BigInt3


def hint(point: EcPoint):
    x = pack(point.x, PRIME)
    y = pack(point.y, PRIME)
    value = slope = ec_double_slope(point=(x, y), alpha=0, p=SECP_P)
