from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_example.XPATH import XpathAvBy


def get_driver(browser_name):
    if browser_name.lower() == 'chrome':
        driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name.lower() == 'edge':
        driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.EDGE)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    return driver, wait


def authorization_setup(login=None, password=None, xpath=None):
    driver, wait = get_driver('firefox')
    driver.get("https://av.by/login/")

    login_field = driver.find_element_by_xpath(XpathAvBy.INPUT_LOGIN)
    login_field.send_keys(login)

    password_field = driver.find_element_by_xpath(XpathAvBy.INPUT_PASSWORD)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    return driver


def teardown(driver):
    driver.quit()


def test_authorization():
    driver = authorization_setup(login='vlad.zver@tyt.by', password='135790qwe', xpath=XpathAvBy.USER_BAR)
    assert driver.find_element_by_xpath(XpathAvBy.USER_BAR)
    driver.quit()


def test_authorization_wrong_login():
    driver = authorization_setup(login='vlad.zver@t', password='135790qwe', xpath=XpathAvBy.ERROR_MESSAGE)
    assert driver.find_element_by_xpath(XpathAvBy.ERROR_MESSAGE)
    driver.quit()


def test_authorization_wrong_password():
    driver = authorization_setup(login='vlad.zver@tyt.by', password='135790', xpath=XpathAvBy.ERROR_MESSAGE)
    assert driver.find_element_by_xpath(XpathAvBy.ERROR_MESSAGE)
    driver.quit()
