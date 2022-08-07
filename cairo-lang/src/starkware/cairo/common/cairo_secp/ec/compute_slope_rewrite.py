# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/cairo_secp/ec.cairo#L94

from starkware.cairo.common.cairo_secp.secp_utils import SECP_P, pack
from starkware.python.math_utils import line_slope

PRIME = 2**251 + 17 * 2**192 + 1


class BigInt3:
    d0: int  # felt
    d1: int  # felt
    d2: int  # felt


class EcPoint:
    x: BigInt3
    y: BigInt3


def hint(point0: EcPoint, point1: EcPoint):
    # Compute the slope.
    x0 = pack(point0.x, PRIME)
    y0 = pack(point0.y, PRIME)
    x1 = pack(point1.x, PRIME)
    y1 = pack(point1.y, PRIME)
    value = slope = line_slope(point1=(x0, y0), point2=(x1, y1), p=SECP_P)
