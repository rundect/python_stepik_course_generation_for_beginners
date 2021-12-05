def interesting_sorting(elem):
    total = 0
    for i in elem:
        total += int(i)
    return total


s = input().split()

sorted_list = sorted(s, key=interesting_sorting)
print(*sorted_list)