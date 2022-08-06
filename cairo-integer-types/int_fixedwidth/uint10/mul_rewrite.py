# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/edf804eb00b585f3f20e22f8318b5297dc8a043f/int_fixedwidth/uint10.cairo#L79

class Int:
    value: int  # felt


def hint(a: Int, b: Int, SHIFT: int = 2**10):
    # Calculate a * b
    m_value = a.value * b.value
    # Do the division
    (m_overflow, m_res) = divmod(m_value, SHIFT)
