import logging

x = 105

logger = logging.getLogger(__name__)


# TODO[agorozhanko 14.10.2020]: logger настраивается для всего модуля, а не в каждой функции
# TODO[vandreychyk 15.10.2020]: настроил logger для всего модуля
def sayHello():
    logger.info('Привет, Мир!')
    return 'Привет, Мир!'


def printMax(a, b):
    if a > b:
        logger.info('%s максимально' % a)
        max = a
    elif a == b:
        logger.info('%s равно %s' % (a, b))
        max = a
    else:
        logger.info('%s максимально' % b)
        max = b
    return max


def func(x):
    logger.info('x  равен %s' % x)
    a = x
    x = 2
    logger.info('Замена локального x на %s' % x)
    return a, x


def func_global():
    global x
    a = x

    logger.info('x равно %s' % x)
    x = 2
    logger.info('Заменяем глобальное значение х на %s' % x)
    return a, x


def func_outer():
    x = 2
    a = x
    logger.info('х равно %s' % x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    logger.info('Локальное х сменилось на %s' % x)
    return a, x


# TODO[agorozhanko 14.10.2020]: нужно оптимизировать код
# TODO[vandreychyk 14.10.2020]: код оптимизировал
def say(message, times=1):
    logger.info(message * times)
    return message, times, message * times


# TODO[agorozhanko 14.10.2020]: нужно оптимизировать код
# TODO[vandreychyk 14.10.2020]: код оптимизировал
def func_key(a, b=5, c=10):
    logger.info('а равно %s, b равно %s, а с равно %s' % (a, b, c))
    return a, b, c


# TODO[agorozhanko 14.10.2020]: нужно оптимизировать код
# TODO[vandreychyk 14.10.2020]: код оптимизировал
def total(a=5, *numbers, **phonebook):
    logger.info(a)

    items = []
    for single_item in numbers:
        logger.info(single_item)
        items.append(single_item)

    for first_part, second_part in phonebook.items():
        logger.info((first_part, second_part))
    return a, items, phonebook


def total_only(initial=5, *numbers, extra_number=1):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    logger.info(count)
    return count


def maximum(x, y):
    if x > y:
        logger.info(x)
        return x
    elif x == y:
        logger.info('Числа равны.')
        return x
    else:
        logger.info(y)
        return y


# TODO[agorozhanko 14.10.2020]: название нужно исправить
# TODO[vandreychyk 14.10.2020]: название исправил
def print_max_desc(x, y):
    """Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами."""
    x = int(x)
    y = int(y)

    if x > y:
        logger.info('%s наибольшее' % x)
    else:
        logger.info('наибольшее %s' % y)
