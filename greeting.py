import logging

logger = logging.getLogger(__name__)
# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger
# TODO[vandreychyk 15.10.2020]: заменил
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
