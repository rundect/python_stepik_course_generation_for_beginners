file = open('text.txt')

print(sum(map(int, file.read().split())))

file.close()