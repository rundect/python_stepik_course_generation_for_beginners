from decimal import *
num = Decimal(input())

num_tuple = num.as_tuple()
maximum = max(num_tuple.digits)
minimum = min(num_tuple.digits)


if Decimal(len(num_tuple.digits)) == abs(num.as_tuple().exponent):
    print(maximum + Decimal('0'))
else:
    print(maximum + minimum)
