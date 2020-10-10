# Использование оператора while
number = 23
running = True

while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')

print('Завершение.')

# Использование оператора if
number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю, вы угадали, ')
    print('(хотя и не выиграли никакого приза!)')
elif guess < number:
    print('Нет, загаданное число немного больше этого.')
else:
    print('Нет, загаданное число немного меньше этого.')
    print('Завершено')

# Использование оператора for
for i in range(1, 5):
    print(i)
else:
    print('Цикл for закончен')

# Использование оператора continue
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введенная строка достаточной длины')

# Использование оператора break
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    print('Длина строки : ', len(s))
print('Завершение')
