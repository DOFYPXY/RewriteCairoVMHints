# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/edf804eb00b585f3f20e22f8318b5297dc8a043f/int_fixedwidth/uint10.cairo#L60

(carry, ids.res.value) = divmod(ids.a.value - ids.b.value, ids.SHIFT)
ids.borrow = -carry  # if b > a then carry is -1
