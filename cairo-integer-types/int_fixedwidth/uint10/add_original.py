# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_fixedwidth/uint10.cairo#L44

(ids.carry, ids.res.value) = divmod(ids.a.value + ids.b.value, ids.SHIFT)
