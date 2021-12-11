from functools import reduce

evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)
 
print(evaluate([*map(int, input().split())], int(input())))