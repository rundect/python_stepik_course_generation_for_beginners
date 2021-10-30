import random


def is_valid(guess_number):
    if 0 < guess_number < 101:
        return True
    else:
        return False


def guess_the_number(num):
    counter = 0
    while True:
        guess_number = int(input('Какое число было сгенерировано?: '))
        if is_valid(guess_number):
            if guess_number > num:
                print('Слишком много, попробуйте еще раз')
                counter += 1
            elif guess_number < num:
                print('Слишком мало, попробуйте еще раз')
                counter += 1
            else:
                print('Вы угадали, поздравляем!')
                print(f'Число попыток - {counter}')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
        print()


print("Добро пожаловать в игру 'Угадай число'")
again = 0
while again == 0:
    n = int(input('Введите любое число: '))
    print('...')
    print(f'Генерация случайного числа от 1 до {n}')
    print('...')
    print(f'Случайное число от 1 до {n} сгенерировано')
    rand_num = random.randrange(1, n + 1)
    guess_the_number(rand_num)
    again = int(input('Спасибо, что играли в числовую угадайку. Хотите сыграть еще раз? (0 - да, 1 - нет): '))
print('До скорых встреч)')
