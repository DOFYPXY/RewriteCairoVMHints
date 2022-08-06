# source: https://github.com/bellissimogiorno/cairo-integer-types/blob/main/int_unbounded/biguint.cairo#L225

from biguint_tools import peek_one_num_from, num_add
a = peek_one_num_from(memory, ids.a.ptr)
b = peek_one_num_from(memory, ids.b.ptr)
a_plus_b = num_add(a, b)
ids.res_ptr = segments.gen_arg(a_plus_b)
