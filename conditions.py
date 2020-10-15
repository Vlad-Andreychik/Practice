# Использование оператора while
import logging

number = 23
running = True
logger = logging.getLogger(__name__)
# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger
# TODO[vandreychyk 15.10.2020]: заменил
while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        logger.info('Поздравляю, вы угадали.')
        running = False
    elif guess < number:
        logger.info('Нет, загаданное число немного больше этого.')
    else:
        logger.info('Нет, загаданное число немного меньше этого.')
else:
    logger.info('Цикл while закончен.')

logger.info('Завершение.')

# Использование оператора if
number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    logger.info('Поздравляю, вы угадали, ')
    logger.info('(хотя и не выиграли никакого приза!)')
elif guess < number:
    logger.info('Нет, загаданное число немного больше этого.')
else:
    logger.info('Нет, загаданное число немного меньше этого.')
    logger.info('Завершено')

# Использование оператора for
for i in range(1, 5):
    logger.info(i)
else:
    logger.info('Цикл for закончен')

# Использование оператора continue
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        logger.info('Слишком мало')
        continue
    logger.info('Введенная строка достаточной длины')

# Использование оператора break
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    logger.info('Длина строки : ', len(s))
logger.info('Завершение')
