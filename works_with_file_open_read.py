file = open('prices.txt')

sum = 0
for line in file:
    name, count, price = line.split()
    sum += int(count) * int(price)
print(sum)
file.close()
