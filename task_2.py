# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте, как наделить бота ""интеллектом""

from random import *
import os


welcome_text = ('Добро пожаловать!\n'
                'Это игра для двоих, поэтому не забудьте позвать своего друга.\n'
                'Можно и врага, выигрывать будет приятнее. >)\n'
                'А если Вы ещё любите сладкое, то игра точно для Вас! :)\n'
                'Теперь немного о правилах:\n'
                'Вам на двоих даётся 2021 конфета. После жеребьёвки вы поочереди начинаете брать конфеты.\n'
                'Но есть важное условие - за один ход нельзя взять больше 28 конфет.\n'
                'Побеждает тот, кто последний забирает все оставшиеся конфеты.\n'
                'Итак, начнём.')
print(welcome_text)

def player_vs_player():
    all_sweets = 2021
    max_sweets = 28
    count = 0
    player_1 = input('Назови своё имя: ')
    player_2 = input('Назови имя своего соперника: ')

    print(f'\n{player_1} vs {player_2}\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'{lucky}, ты ходишь первым! Поехали!')

    while all_sweets > 0:
        if count == 0:
            step = int(input(f'\n{lucky}, твой ход: '))
            if step > all_sweets or step > max_sweets:
                step = int(input(f'\nАтата. Можно взять только {all_sweets} конфет, {lucky}. Давай ещё раз: '))
            all_sweets = all_sweets - step
        if all_sweets > 0:
            print(f'\nОсталось ещё {all_sweets} конфет.')
            count = 1
        else:
            print('Конфет больше нет :(')

        if count == 1:
            step = int(input(f'\n{loser}, твой ход: '))
            if step > all_sweets or step > max_sweets:
                step = int(input(f'\nАтата. Можно взять только {all_sweets} конфет, {loser}. Давай ещё раз: '))
            all_sweets = all_sweets - step
        if all_sweets > 0:
            print(f'\nОсталось ещё {all_sweets} конфет.')
            count = 0
        else:
            print('Конфет больше нет :(')

    if count == 1:
        print(f'Победил {loser}. Поздравляю!')
    if count == 0:
        print(f'Победил {lucky}. Поздравляю!')

player_vs_player()


def player_vs_bot():
    all_sweets = 2021
    max_sweets = 28
    player_1 = input('\nНазови своё имя: ')
    player_2 = 'Бот'
    players = [player_1, player_2]
    print(f'\n{player_1} vs {player_2}\n')
    print('\nКто начинает первый?\n')

    lucky = randint(-1, 0)

    print(f'{players[lucky+1]}, ты ходишь первым. Поехали!')

    while all_sweets > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(f'\nОсталось {all_sweets} конфет. \n{players[lucky%2]}, твой ход: ')

            if all_sweets < 29:
                step = all_sweets
            else:
                delenie = all_sweets // 28
                step = all_sweets - ((delenie * max_sweets) + 1)
                if step == -1:
                    step = max_sweets -1
                if step == 0:
                    step = max_sweets
            while step > 28 or step < 1:
                step = randint(1, 28)
            print(step)
        else:
            step = int(input(f'\nОсталось {all_sweets} конфет. \n{players[lucky%2]}, твой ход: '))
            while step > max_sweets or step > all_sweets:
                step = int(input(f'\nАтата. Можно взять только {all_sweets} конфет. Давай ещё раз: '))
        all_sweets = all_sweets - step

    print(f'Осталось {all_sweets} конфет. \n{players[lucky%2]}, ты победил. Поздравляю!')

player_vs_bot()