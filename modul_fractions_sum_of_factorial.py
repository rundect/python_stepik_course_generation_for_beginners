
from fractions import Fraction
from math import factorial

total = 0
for i in range(int(input())):
    total += Fraction(1, (factorial(i + 1)))
print(total)
