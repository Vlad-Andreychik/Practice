INPUT_LOGIN = '//input[@id="login"]'
INPUT_PASSWORD = '//input[@id="password"]'
USER_BAR = '//li[@class="nav__item nav__item--dropdown nav__item--user"]'
ERROR_MESSAGE = '//div[@class ="error-message"]'
SEARCH = '//button[@id="submit_presearch"]'
PRODUCE_YEAR = '//div[@class="dropselect-head js-dropselect-head dropselect-head-year"]'
LISTING_TITLE = '//h3[@class="listing__title"]'


def brand(name):
    return '//option[text()="{}"]'.format(name)


def model_auto(model):
    return '//option[text()="{}"]'.format(model)


def year_from(year):
    return '//select[@name="year_from"]/option[text()="{}"]'.format(year)


def year_to(year):
    return '//select[@name="year_to"]/option[text()="{}"]'.format(year)
