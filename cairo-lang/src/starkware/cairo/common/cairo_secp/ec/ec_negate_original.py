from starkware.cairo.common.cairo_secp.secp_utils import SECP_P, pack

y = pack(ids.point.y, PRIME) % SECP_P
# The modulo operation in python always returns a nonnegative number.
value = (-y) % SECP_P
