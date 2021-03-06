import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('..//logs//additionally.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_error_details():
    return 2, 'описание ошибки №2'


def using_lambda():
    points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
    points.sort(key=lambda i: i['y'])
    logger.info(points)


def list_comprehension():
    list_one = [2, 3, 4]
    list_two = [2 * i for i in list_one if i > 2]
    logger.info(list_two)


def power_sum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


def using_assert():
    my_list = ['item']
    assert len(my_list) >= 1
    logger.info(my_list.pop())
    logger.info(my_list)
    assert len(my_list) >= 1

# spisok = ['s.brel_dolls', 'afcspark', 'thecooltravell', 'maks_trololo', 'denchik_kozlovsky',
#           'razinkov.nik', 'mmockingbirdd', 'alienzombiie', 'your_shev', 'klimuts', 'ivan.brel',
#           '_sh_andrew', 'me_reak_', 'romanovskii_n', 'lazhik_51k', 'vadik_grebnev', 'slava.noker',
#           'natalia_khovanskih', 'stakford', 'vlad1k_23', 'krich_sergey', 'anton_captain_spark',
#           'lug_rom', 'tan_pan1788', 'boriseviche97', 'davai_tak88', 'stepankerus', 'antonbudzila',
#           'katherina_d', 'eugene_eki', 'kerunak', 'katrinn_pinchuk', 'ruslannazarenko23',
#           'pimanelli', 'yulka_pavlova18', 'mari.smrnv', 'katty_aulova', 'rnvsk_xx', 'kr.blnv',
#           'andreichik.viktoria', 'kkrichevtsova', 'elenaair', 'miityaaa', 'aneleair', 'mari_andre',
#           'alexey_banchuk', 'e.parkhomenka', 'gkonoplich', 'inastassi', 'sanchos_sh', 'diandrey',
#           'da71lenko', 'vlad_kutsarenko', 'ratmir.kenzheev', 'olepinchuk', 'maksimoptimus_goraim',
#           'bayer17foryou']
