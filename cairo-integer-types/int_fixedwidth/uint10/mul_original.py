# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/edf804eb00b585f3f20e22f8318b5297dc8a043f/int_fixedwidth/uint10.cairo#L79

# Calculate a * b
m_value = ids.a.value * ids.b.value
# Do the division
(ids.m_overflow, ids.m_res) = divmod(m_value, ids.SHIFT)
