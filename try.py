import math
import random

print(math.isclose(10.0000001, 10.000000000002, rel_tol=0.0001))

pos = 2
a = 6
a &= (1<<pos)
a &= (1<<pos)
print(a)