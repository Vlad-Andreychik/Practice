import logging
import os
import platform
import sys
import warnings


# TODO[agorozhanko 16.10.2020]: код в модуле не компилируется
def version_check():
    if sys.version_info[0] < 3:
        warnings.warn("Для выполнения этой программы необходима как минимум \
    версия Python 3.0",
                      RuntimeWarning)
    else:
        print('Нормальное продолжение')


# TODO[agorozhanko 16.10.2020]:для внесения изменений в код нужно использовать функции рефакторинга
versioncheck()


def use_logging():
    if platform.platform().startswith('Windows'):
        logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                    os.getenv('HOMEPATH'),
                                    'test.log')
    else:
        logging_file = os.path.join(os.getenv('HOME'), 'test.log')
    print("Сохраняем лог в", logging_file)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename=logging_file,
    )
    logging.debug("Начало программы")
    logging.info("Какие-то действия")
    logging.warning("Программа умирает")
