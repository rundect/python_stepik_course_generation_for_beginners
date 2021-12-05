def comparator(n):
    return sum([int(i) for i in str(n)]), n

numbers = [int(i) for i in input().split()]

print(*sorted(numbers, key=comparator))