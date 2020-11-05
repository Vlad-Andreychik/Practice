# Авторизация пользователя
INPUT_LOGIN = '//input[@id="login"]'
INPUT_PASSWORD = '//input[@id="password"]'

# Страница пользователя
USER_BAR = '//li[@class="nav__item nav__item--dropdown nav__item--user"]'

# Сообщения
ERROR_MESSAGE = '//div[@class ="error-message"]'
EMPTY_SEARCH = '//h2[text()="Мы не нашли объявлений по вашему запросу"]'

# Кнопки
SEARCH = '//button[@id="submit_presearch"]'
PRODUCE_YEAR = '//div[@class="dropselect-head js-dropselect-head dropselect-head-year"]'

# Результат поиска
LISTING_TITLE = '//h3[@class="listing__title"]'
LISTING_CONTAINER = '//div[@class="listing__container"]'
LISTING_ITEMS = '//div[@class="listing-item"]'


# Параметры поиска
def get_brand(name):
    """
    Возвращает xpath марки авто
    """
    return '//option[text()="{}"]'.format(name)


def get_model_auto(model):
    """
    Возвращает xpath модели марки авто
    """
    return '//select[@id="model_id"]/option[text()="{}"]'.format(model)


def get_year_from(year):
    """
    Возвращает xpath года выпуска с
    """
    return '//select[@name="year_from"]/option[text()="{}"]'.format(year)


def year_to(year):
    """
        Возвращает xpath года выпуска по
    """
    return '//select[@name="year_to"]/option[text()="{}"]'.format(year)
