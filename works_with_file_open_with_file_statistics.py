with open('file.txt', encoding='utf-8') as file:
    quantity_of_letters = 0
    quantity_of_words = 0
    quantity_of_rows = 0
    for i in file.readlines():
        for j in i:
            if j.isalpha():
                quantity_of_letters += 1
        quantity_of_words += len(i.split())
        quantity_of_rows += 1
    print(f'Input file contains:\n{quantity_of_letters} letters\n{quantity_of_words} words\n{quantity_of_rows} lines')
