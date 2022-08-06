# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_unbounded/biguint.cairo#L225

# **Incompleted!**
# TODO: translate user-defined lib functions

class RelocatableValue:
    segment_index: int
    offset: int


class BigUint:
    ptr: RelocatableValue  # felt*


def hint(a: BigUint, b: BigUint):
    # from biguint_tools import peek_one_num_from, num_add
    a = peek_one_num_from(memory, a.ptr)
    b = peek_one_num_from(memory, b.ptr)
    a_plus_b = num_add(a, b)
    res_ptr = segments.gen_arg(a_plus_b)
