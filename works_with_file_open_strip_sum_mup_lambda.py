file = open('text.txt')

print(sum(map(lambda x: int(x.strip()), filter(lambda x: x.strip(), file))))

file.close()