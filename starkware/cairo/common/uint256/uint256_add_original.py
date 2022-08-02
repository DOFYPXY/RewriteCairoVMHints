sum_low = ids.a.low + ids.b.low
ids.carry_low = 1 if sum_low >= ids.SHIFT else 0
sum_high = ids.a.high + ids.b.high + ids.carry_low
ids.carry_high = 1 if sum_high >= ids.SHIFT else 0
