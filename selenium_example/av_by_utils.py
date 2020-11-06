from selenium_example import selenium_utils as su
from selenium_example import xpath as sxpath


def search_auto(driver, brand, model='Любая', year_from='с', year_to='по'):
    """Метод осуществляет поиск авто по заданным параметрам

    :param driver: веб-драйвер
    :param brand: марка авто
    :param model: модель марки авто
    :param year_from: год выпуска с
    :param year_to: год выпуска по
    """
    select_brand(driver, brand)
    select_model(driver, model)
    select_year(driver, year_from, year_to)

    search(driver)


def select_brand(driver, name):
    """
    Метод выбирает марку авто

    :param driver: веб-драйвер
    :param name: название марки авто
    """
    su.click_element(driver, sxpath.get_brand(name))


def select_model(driver, model='Любая'):
    """
    Метод выбирает модель марки авто

    :param driver: веб-драйвер
    :param model: модель марки авто
    """
    su.click_element(driver, sxpath.get_model_auto(model))


def select_year(driver, year_from='с', year_to='по'):
    """
    Метод выбирает годы выпуска

    :param driver: веб-драйвер
    :param year_from: год выпуска с
    :param year_to: год выпуска по
    """
    su.click_element(driver, sxpath.PRODUCE_YEAR)
    su.click_element(driver, sxpath.get_year_from(year_from))
    su.click_element(driver, sxpath.year_to(year_to))


def search(driver):
    """
    Метод осуществляет поиск

    :param driver: веб-драйвер
    """
    su.click_element(driver, sxpath.SEARCH)


def authorization(driver, login, password):
    """
    Метод осуществляет авторизацию на сайте

    :param driver: веб-драйвер
    :param login: логин
    :param password: пароль
    """
    login_input(driver, login)
    password_input(driver, password)

    submit(driver)


def login_input(driver, login):
    """
    Метод вводит логин

    :param driver: веб-драйвер
    :param login: логин
    """
    su.send_keys_element(driver, sxpath.INPUT_LOGIN, login)


def password_input(driver, password):
    """
    Метод вводит пароль

    :param driver: веб-драйвер
    :param password: пароль
    """
    su.send_keys_element(driver, sxpath.INPUT_PASSWORD, password)


def submit(driver):
    """Метод осуществляет вход"""
    su.click_element(driver, sxpath.SUBMIT)
