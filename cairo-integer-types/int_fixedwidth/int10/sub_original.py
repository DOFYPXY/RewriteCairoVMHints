# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/int10.cairo#L86

a_sub_b = (ids.a.value - ids.b.value) % PRIME
if (a_sub_b >= ids.SHIFT) and (a_sub_b < 2*ids.SHIFT):
    (ids.overflow, ids.res.value) = (1, (a_sub_b - 2 * ids.SHIFT) % PRIME)
elif (a_sub_b < PRIME - ids.SHIFT) and (PRIME - 2 * ids.SHIFT <= a_sub_b):
    (ids.overflow, ids.res.value) = (-1 %
                                     PRIME, (a_sub_b + 2 * ids.SHIFT) % PRIME)
else:
    (ids.overflow, ids.res.value) = (0, a_sub_b)
