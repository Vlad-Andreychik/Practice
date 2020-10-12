import logging

x = 105


def sayHello():
    logger = logging.getLogger("exampleApp.functions.sayHello")
    logger.info('Привет, Мир!')


def printMax(a, b):
    logger = logging.getLogger("exampleApp.functions.printMax")
    if a > b:
        logger.info('%s максимально' % (a))
    elif a == b:
        logger.info('%s равно %s' % (a, b))
    else:
        logger.info('%s максимально' % (b))


def func(x):
    logger = logging.getLogger("exampleApp.functions.func")
    logger.info('x  равен %s' % (x))
    x = 2
    logger.info('Замена локального x на %s' % (x))


def func_global():
    logger = logging.getLogger("exampleApp.functions.func_global")
    global x

    logger.info('x равно %s' % (x))
    x = 2
    logger.info('Заменяем глобальное значение х на %s', (x))


def func_outer():
    logger = logging.getLogger("exampleApp.functions.func_outer")
    x = 2
    logger.info('х равно %s' % (x))

    def func_inner():
        logger = logging.getLogger("exampleApp.func_inner")
        nonlocal x
        x = 5

    func_inner()
    logger.info('Локальное х сменилось на %s' % (x))


def say(message, times=1):
    logger = logging.getLogger("exampleApp.functions.say")
    logger.info(message * times)


def func_key(a, b=5, c=10):
    logger = logging.getLogger("exampleApp.functions.func_key")
    logger.info('а равно %s, b равно %s, а с равно %s' % (a, b, c))


def total(a=5, *numbers, **phonebook):
    logger = logging.getLogger("exampleApp.functions.total")
    logger.info(a)

    for single_item in numbers:
        logger.info(single_item)

    for first_part, second_part in phonebook.items():
        logger.info((first_part, second_part))


def total_only(initial=5, *numbers, extra_number):
    logger = logging.getLogger("exampleApp.functions.total_only")
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    logger.info(count)


def maximum(x, y):
    logger = logging.getLogger("exampleApp.functions.total")
    if x > y:
        logger.info(x)
    elif x == y:
        logger.info('Числа равны.')
    else:
        logger.info(y)


def printMax_desc(x, y):
    """Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами."""
    logger = logging.getLogger("exampleApp.functions.total")
    x = int(x)
    y = int(y)

    if x > y:
        logger.info('%s наибольшее' % (x))
    else:
        logger.info('наибольшее' % (y))
