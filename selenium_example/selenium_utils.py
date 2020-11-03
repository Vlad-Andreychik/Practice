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

chrome_driver = 'D:\vandreychik\Practice\selenium_example\chromedriver.exe'
url = 'https://av.by/login/'


def get_driver(browser_name):
    browser = browser_name.lower()
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=chrome_driver)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise TypeError('Данный тип браузера не поддерживается')
    driver.maximize_window()
    return driver


def go_to_url(driver):
    driver.get(url)


def wait_element(driver, xpath):
    wait = WebDriverWait(driver, 10)

    element = None
    attempts = 3
    while attempts != 0:
        try:
            element = wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            attempts -= 1
    return element


def click_element(driver, xpath):
    element = wait_element(driver, xpath)
    if element is not None:
        element.click()
