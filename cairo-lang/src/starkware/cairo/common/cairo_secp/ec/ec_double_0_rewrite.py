# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/cairo_secp/ec.cairo#L142

from starkware.cairo.common.cairo_secp.secp_utils import SECP_P, pack

PRIME = 2**251 + 17 * 2**192 + 1


class BigInt3:
    d0: int  # felt
    d1: int  # felt
    d2: int  # felt


class EcPoint:
    x: BigInt3
    y: BigInt3


def hint(point: EcPoint):
    slope = pack(slope, PRIME)
    x = pack(point.x, PRIME)
    y = pack(point.y, PRIME)

    value = new_x = (pow(slope, 2, SECP_P) - 2 * x) % SECP_P
