# source: https://github.com/starkware-libs/cairo-lang/blob/master/src/starkware/cairo/common/cairo_secp/ec.cairo#L26


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


def assert_integer(val):
    """
    Asserts that the input is an integer (and not relocatable value).
    """
    assert isinstance(val, int), f"Expected integer, found: {val}."


def as_int(val, prime):
    """
    Returns the lift of the given field element, val, as an integer in the range
    (-prime/2, prime/2).
    """
    assert_integer(val)
    return val if val < prime // 2 else val - prime


def pack(z, prime):
    """
    Takes an UnreducedBigInt3 struct which represents a triple of limbs (d0, d1, d2) of field
    elements and reconstructs the corresponding 256-bit integer (see split()).
    Note that the limbs do not have to be in the range [0, BASE).
    prime should be the Cairo field, and it is used to handle negative values of the limbs.
    """
    limbs = z.d0, z.d1, z.d2
    return sum(as_int(limb, prime) * (BASE**i) for i, limb in enumerate(limbs))


def hint(point: EcPoint):
    y = pack(point.y, PRIME) % SECP_P
    # The modulo operation in python always returns a nonnegative number.
    value = (-y) % SECP_P
