memory[ids.output] = res = (int(ids.value) % PRIME) % ids.base
assert res < ids.bound, f'split_int(): Limb {res} is out of range.'
