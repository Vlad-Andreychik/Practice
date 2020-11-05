import logging

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('..//logs//selenium.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

chrome_driver = 'chromedriver.exe'
firefox_driver = 'geckodriver.exe'
url = 'https://av.by'


def get_driver(browser_name):
    """
    Метод осуществляет настройку веб-драйвера

    :param browser_name: имя браузера
    :return: веб-драйвер
    """
    browser = browser_name.lower()
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=chrome_driver)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=firefox_driver)
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise TypeError('Данный тип браузера не поддерживается')
    driver.maximize_window()
    return driver


def go_to_url(driver):
    """
    Метод осуществляет переход на страницу по URL

    :param driver: веб-драйвер
    """
    driver.get(url)


def wait_element(driver, xpath):
    """
    Метод осуществляет поиск веб-элемента с использованием ожидания

    :param driver: веб-драйвер
    :param xpath: xpath искомого веб-элемента
    :return: веб-элемент
    """
    wait = WebDriverWait(driver, 10)

    element = None
    attempts = 3
    while attempts != 0 and element is None:
        try:
            element = wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            logger.error('Ошибка поиска элемента')
        attempts -= 1
    return element


def click_element(driver, xpath):
    """
    Метод осушествляет нажатие на веб-элемент

    :param driver: веб-драйвер
    :param xpath: xpath веб-элемента
    """
    element = wait_element(driver, xpath)
    if element is not None:
        element.click()
