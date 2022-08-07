from starkware.cairo.common.cairo_secp.secp_utils import SECP_P, pack
from starkware.python.math_utils import line_slope

# Compute the slope.
x0 = pack(ids.point0.x, PRIME)
y0 = pack(ids.point0.y, PRIME)
x1 = pack(ids.point1.x, PRIME)
y1 = pack(ids.point1.y, PRIME)
value = slope = line_slope(point1=(x0, y0), point2=(x1, y1), p=SECP_P)
