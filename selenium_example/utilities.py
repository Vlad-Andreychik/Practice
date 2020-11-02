import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_example.XPATH import brand, ImmutableXpath

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('..//logs//selenium.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_driver(browser_name):
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name.lower() == 'edge':
        driver = webdriver.Edge()
    else:
        return logger.warning('Неверный ввод названия браузера')
    driver.maximize_window()

    return driver


def wait(driver):
    return WebDriverWait(driver, 10)


def select_brand(driver, name):
    wait(driver).until(EC.presence_of_element_located((By.XPATH, brand(name)))).click()


def select_model(driver, model='Любая'):
    wait(driver).until(EC.presence_of_element_located((By.XPATH, model))).click()


def select_year(driver, year_from, year_to):
    wait(driver).until(EC.visibility_of_element_located((By.XPATH, ImmutableXpath.PRODUCE_YEAR))).click()
    wait(driver).until(EC.visibility_of_element_located((By.XPATH, year_from))).click()
    wait(driver).until(EC.visibility_of_element_located((By.XPATH, year_to))).click()


def search(driver):
    wait(driver).until(EC.visibility_of_element_located((By.XPATH, ImmutableXpath.SEARCH))).click()
