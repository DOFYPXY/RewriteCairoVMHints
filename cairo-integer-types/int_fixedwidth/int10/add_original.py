# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/int10.cairo#L62
a_plus_b = (ids.a.value + ids.b.value) % PRIME
if (a_plus_b >= ids.SHIFT) and (a_plus_b < 2*ids.SHIFT):
    (ids.overflow, ids.res.value) = (1, (a_plus_b - 2 * ids.SHIFT) % PRIME)
elif (a_plus_b < PRIME - ids.SHIFT) and (PRIME - 2 * ids.SHIFT <= a_plus_b):
    (ids.overflow, ids.res.value) = (-1 %
                                     PRIME, (a_plus_b + 2 * ids.SHIFT) % PRIME)
else:
    (ids.overflow, ids.res.value) = (0, a_plus_b)
