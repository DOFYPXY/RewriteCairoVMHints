# source: https://github.com/starkware-libs/cairo-lang/blob/13cef109cd811474de114925ee61fd5ac84a25eb/src/starkware/cairo/common/cairo_secp/ec.cairo#L210
from starkware.cairo.common.cairo_secp.secp_utils import SECP_P, pack

PRIME = 2**251 + 17 * 2**192 + 1


class BigInt3:
    d0: int  # felt
    d1: int  # felt
    d2: int  # felt


class EcPoint:
    x: BigInt3
    y: BigInt3


def hint(point0: EcPoint, point1: EcPoint):
    slope = pack(slope, PRIME)
    x0 = pack(point0.x, PRIME)
    x1 = pack(point1.x, PRIME)
    y0 = pack(point0.y, PRIME)
    value = new_x = (pow(slope, 2, SECP_P) - x0 - x1) % SECP_P
