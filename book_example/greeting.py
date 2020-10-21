import logging
# TODO[agorozhanko 16.10.2020]: логер работает?
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
# TODO[agorozhanko 21.10.2020]: не правильное рассширение у файла лога
file_handler = logging.FileHandler('logs//greeting.logs', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def greeting():
    logger.info('Hello world')

    logger.info('''Это многострочная строка. Это её первая строка.
                Это её вторая строка.
                "What's your name?", - спросил я.
                Он ответил: "Bond, James Bond."
                ''')

    age = 21
    name = 'Vlad'
    logger.info('Возраст {0} -- {1} лет'.format(name, age))
    i = 5
    logger.info(i)
    i = i + 1
    logger.info(i)
    a = 2
    a = a * 3
    logger.info(a)
    return a, i, name, age
