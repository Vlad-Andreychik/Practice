import logging

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import selenium_example.XPATH as sxpath

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
        raise TypeError('Ошибка ввода имени браузера')
    driver.maximize_window()

    return driver


def wait(driver):
    return WebDriverWait(driver, 10)


def select(driver, xpath):
    attempts = 3
    while attempts != 0:
        try:
            return wait(driver).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            attempts -= 1


def select_click(select):
    if select:
        select.click()


def select_brand(driver, name):
    wait(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.brand(name)))).click()


def select_model(driver, model='Любая'):
    wait(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.model_auto(model)))).click()


def select_year(driver, year_from='с', year_to='по'):
    wait(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.PRODUCE_YEAR))).click()
    wait(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.year_from(year_from)))).click()
    wait(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.year_to(year_to)))).click()


def search(driver):
    wait(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.SEARCH))).click()
