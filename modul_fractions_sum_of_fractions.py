
from fractions import Fraction


total = 0
for i in range(int(input())):
    total += Fraction(1, ((i + 1) ** 2))
print(total)
