import logging
import os
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
# TODO[agorozhanko 21.10.2020]: не правильное рассширение у файла лога
file_handler = logging.FileHandler('logs//tasks.logs', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# TODO[agorozhanko 21.10.2020]:всё ещё используются абсолютные пути
def backup_date_plus_time_file_name():
    source = ['C:\\Users', 'G:\\kyrs']

    target_dir = 'G:\\Backup'

    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

    zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
    logger.info(zip_command)
    if os.system(zip_command) == 0:
        logger.info('Резервная копия успешно создана в', target)
    else:
        logger.info('Создание резервной копии НЕ УДАЛОСЬ')


def backup_time_file_name():
    import os
    import time

    source = ['C:\\Users', 'G:\\kyrs']

    target_dir = 'G:\\Backup'

    today = target_dir + os.sep + time.strftime('%Y%m%d')

    now = time.strftime('%H%M%S')

    if not os.path.exists(today):
        os.mkdir(today)
    logger.info('Каталог успешно создан', today)

    target = today + os.sep + now + '.zip'

    zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

    if os.system(zip_command) == 0:
        logger.info('Резервная копия успешно создана в', target)
    else:
        logger.info('Создание резервной копии НЕ УДАЛОСЬ')


def backup_with_comment():
    source = ['C:\\Users', 'G:\\kyrs']

    target_dir = 'G:\\Backup'

    today = target_dir + os.sep + time.strftime('%Y%m%d')

    now = time.strftime('%H%M%S')
    comment = input('Введите комментарий --> ')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + \
                 comment.replace(' ', '_') + '.zip'

    if not os.path.exists(today):
        os.mkdir(today)
    logger.info('Каталог успешно создан', today)

    zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

    if os.system(zip_command) == 0:
        logger.info('Резервная копия успешно создана в', target)
    else:
        logger.info('Создание резервной копии НЕ УДАЛОСЬ')
