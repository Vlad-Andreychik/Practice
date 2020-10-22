import logging
import os
import platform
import sys
import warnings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
# TODO[agorozhanko 21.10.2020]: не правильное рассширение у файла лога
# TODO[vandreychyk 22.10.2020]: исправил
file_handler = logging.FileHandler('..//logs//standard_libs.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def version_check():
    if sys.version_info[0] < 3:
        warnings.warn("Для выполнения этой программы необходима как минимум \
    версия Python 3.0",
                      RuntimeWarning)
    else:
        logging.info('Нормальное продолжение')


version_check()


def use_logging():
    if platform.platform().startswith('Windows'):
        logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                    os.getenv('HOMEPATH'),
                                    'test.logs')
    else:
        logging_file = os.path.join(os.getenv('HOME'), 'test.logs')
    logging.info("Сохраняем лог в", logging_file)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename=logging_file,
    )
    logging.debug("Начало программы")
    logging.info("Какие-то действия")
    logging.warning("Программа умирает")
