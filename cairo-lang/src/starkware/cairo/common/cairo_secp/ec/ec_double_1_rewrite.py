from starkware.cairo.common.cairo_secp.secp_utils import SECP_P

PRIME = 2**251 + 17 * 2**192 + 1


class BigInt3:
    d0: int  # felt
    d1: int  # felt
    d2: int  # felt


class EcPoint:
    x: BigInt3
    y: BigInt3


def hint(slope: BigInt3, new_x: BigInt3, x, y):
    value = new_y = (slope * (x - new_x) - y) % SECP_P
