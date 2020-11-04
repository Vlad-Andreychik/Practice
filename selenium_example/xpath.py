INPUT_LOGIN = '//input[@id="login"]'
INPUT_PASSWORD = '//input[@id="password"]'
USER_BAR = '//li[@class="nav__item nav__item--dropdown nav__item--user"]'
ERROR_MESSAGE = '//div[@class ="error-message"]'
SEARCH = '//button[@id="submit_presearch"]'
PRODUCE_YEAR = '//div[@class="dropselect-head js-dropselect-head dropselect-head-year"]'
LISTING_TITLE = '//h3[@class="listing__title"]'
EMPTY_SEARCH = '//h2[text()="Мы не нашли объявлений по вашему запросу"]'
LISTING_CONTAINER = '//div[@class="listing__container"]'
LISTING_ITEMS = '//div[@class="listing-item"]'


def get_brand(name):
    return '//option[text()="{}"]'.format(name)


def get_model_auto(model):
    return '//select[@id="model_id"]/option[text()="{}"]'.format(model)


def get_year_from(year):
    return '//select[@name="year_from"]/option[text()="{}"]'.format(year)


def year_to(year):
    return '//select[@name="year_to"]/option[text()="{}"]'.format(year)
