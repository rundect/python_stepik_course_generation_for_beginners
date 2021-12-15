file = open('numbers.txt')

print(sum(map(int, file)))

file.close()