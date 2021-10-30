import random


def generate_password(len_of_pass, chars):
    created_pass = []
    for i in range(len_of_pass):
        created_pass += random.choice(chars)
    return created_pass


question = '(0 - да, любой другой символ - нет): '
digits = [i for i in '0123456789']
lowercase_letters = [i for i in 'abcdefghijklmnopqrstuvwxyz']
uppercase_letters = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
punctuation = [i for i in '!#$%&*+-=?@^_']
ambiguous_characters = [i for i in 'il1Lo0O']
chars = []

quantity_of_pass = int(input('Количество паролей для генерации: '))
len_of_pass = int(input('Длина  одного пароля: '))
include_digits = int(input(f'Включать ли цифры (0123456789)? {question}'))
include_u_letters = int(input(f'Включать ли прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? {question}'))
include_l_letters = int(input(f'Включать ли строчные буквы (abcdefghijklmnopqrstuvwxyz)? {question}'))
include_chars = int(input(f'Включать ли символы (!#$%&*+-=?@^_)? {question}'))
exclude_chars = int(input(f'Исключать ли неоднозначные символы (il1Lo0O)? {question}'))

if include_digits == 0:
    chars.extend(digits)
if include_u_letters == 0:
    chars.extend(uppercase_letters)
if include_l_letters == 0:
    chars.extend(lowercase_letters)
if include_chars == 0:
    chars.extend(punctuation)
if exclude_chars == 0:
    for i in ambiguous_characters:
        if i in chars:
            chars.remove(i)

for i in range(quantity_of_pass):
    password = generate_password(len_of_pass, chars)
    print(*password, sep='')
