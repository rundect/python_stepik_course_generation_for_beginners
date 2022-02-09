with open('numbers.txt', encoding='utf-8') as file:
    for i in file.readlines():
        total = 0
        for j in i.split():
            total += int(j)
        print(total)
