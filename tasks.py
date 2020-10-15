import os
import time
import logging


# TODO[agorozhanko 14.10.2020]:нужно заменить print на logger

def backup_ver1():
    source = ['C:\\Users', 'G:\\kyrs']

    target_dir = 'G:\\Backup'

    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

    zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
    logger.info(zip_command)
    if os.system(zip_command) == 0:
        logger.info('Резервная копия успешно создана в', target)
    else:
        logger.info('Создание резервной копии НЕ УДАЛОСЬ')


def backup_ver2():
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


def backup_ver3():
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
