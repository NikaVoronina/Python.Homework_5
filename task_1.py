# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = input ('Введите текст через пробел: ')
print(f'Исходный текст: { text }')
find_text = 'абв'
list = [i for i in text.split() if find_text not in i]
print(f'Итог: {" ".join(list)}')