with open('lines.txt', encoding='utf-8') as file:
    len_of_word = len(max(file.readlines(), key=len))
    file.seek(0)
    for i in file:
        if len(i) == len_of_word:
            print(i.rstrip('\n'))
