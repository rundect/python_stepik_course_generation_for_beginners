def print_products(*args):
    counter = 0
    for i in args:
        if isinstance(i, str) and i:
            counter += 1
            print(f'{counter}) {i}')

    if counter == 0:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)