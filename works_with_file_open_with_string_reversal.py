
with open('data.txt', encoding='utf-8') as file:
    for i in file.readlines()[::-1]:
        print(i.rstrip('\n'))
