from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

from selenium_example.XPATH import xpath_av_by


def get_driver(browser_name):
    if browser_name.lower() == 'chrome':
        driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.EDGE)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def test_request_not_found():
    driver = get_driver('firefox')
    driver.get("https://av.by/")

    car_brand = driver.find_element_by_xpath(xpath_av_by.AUDI)
    car_brand.click()

    car_model = driver.find_element_by_xpath(xpath_av_by.AUDI_100)
    car_model.click()

    produce_year = driver.find_element_by_xpath(xpath_av_by.PRODUCE_YEAR)
    produce_year.click()

    produce_year_from = driver.find_element_by_xpath(xpath_av_by.PRODUCE_YEAR_FROM)
    produce_year_from.click()

    search = driver.find_element_by_xpath(xpath_av_by.SEARCH)
    search.click()

    assert "Мы не нашли объявлений по вашему запросу" in driver.page_source
    driver.quit()


def test_request_found():
    driver = get_driver('firefox')
    driver.get("https://av.by/")

    car_brand = driver.find_element_by_xpath(xpath_av_by.AUDI)
    car_brand.click()

    car_model = driver.find_element_by_xpath(xpath_av_by.AUDI_100)
    car_model.click()

    search = driver.find_element_by_xpath(xpath_av_by.SEARCH)
    search.click()

    assert driver.find_element_by_xpath(xpath_av_by.LISTING_TITLE)
    driver.quit()


def test_authorization():
    driver = get_driver('firefox')
    driver.get("https://av.by/login/")

    login = driver.find_element_by_xpath(xpath_av_by.INPUT_LOGIN)
    login.send_keys('vlad.zver@tyt.by')

    password = driver.find_element_by_xpath(xpath_av_by.INPUT_PASSWORD)
    password.send_keys('135790qwe')
    password.send_keys(Keys.RETURN)

    assert driver.find_element_by_xpath(xpath_av_by.USER_BAR)
    driver.quit()


def test_authorization_wrong_login():
    driver = get_driver('firefox')
    driver.get("https://av.by/login/")

    login = driver.find_element_by_xpath(xpath_av_by.INPUT_LOGIN)
    login.send_keys('vlad.zver@t')

    password = driver.find_element_by_xpath(xpath_av_by.INPUT_PASSWORD)
    password.send_keys('135790qwe')
    password.send_keys(Keys.RETURN)

    assert driver.find_element_by_xpath(xpath_av_by.ERROR_MESSAGE)
    driver.quit()


def test_authorization_wrong_password():
    driver = get_driver('firefox')
    driver.get("https://av.by/login/")

    login = driver.find_element_by_xpath(xpath_av_by.INPUT_LOGIN)
    login.send_keys('vlad.zver@tyt.by')

    password = driver.find_element_by_xpath(xpath_av_by.INPUT_PASSWORD)
    password.send_keys('135790')
    password.send_keys(Keys.RETURN)

    assert driver.find_element_by_xpath(xpath_av_by.ERROR_MESSAGE)
    driver.quit()
