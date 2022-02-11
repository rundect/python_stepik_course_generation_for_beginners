
from fractions import Fraction

n = int(input())
old_fraction = 0
for i in range(1, n):
    if i < n - i:
        fraction = Fraction(i, n - i)
        if fraction > old_fraction and (fraction.numerator + fraction.denominator == n):
            old_fraction = fraction
print(old_fraction)
