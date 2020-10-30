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


def request_setup(brand=None, model=None, year_from=None):
    driver = get_driver('firefox')
    driver.get("https://av.by/")

    car_brand = driver.find_element_by_xpath(brand)
    car_brand.click()

    car_model = driver.find_element_by_xpath(model)
    car_model.click()

    if year_from is not None:
        produce_year = driver.find_element_by_xpath(xpath_av_by.PRODUCE_YEAR)
        produce_year.click()
        produce_year_from = driver.find_element_by_xpath(year_from)
        produce_year_from.click()
    return driver


def authorization_setup(login=None, password=None):
    driver = get_driver('firefox')
    driver.get("https://av.by/login/")

    login_field = driver.find_element_by_xpath(xpath_av_by.INPUT_LOGIN)
    login_field.send_keys(login)

    password_field = driver.find_element_by_xpath(xpath_av_by.INPUT_PASSWORD)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    return driver


def test_request_not_found():
    driver = request_setup(brand=xpath_av_by.AUDI,
                           model=xpath_av_by.AUDI_100,
                           year_from=xpath_av_by.PRODUCE_YEAR_FROM)

    search = driver.find_element_by_xpath(xpath_av_by.SEARCH)
    search.click()

    assert "Мы не нашли объявлений по вашему запросу" in driver.page_source
    driver.quit()


def test_request_found():
    driver = request_setup(brand=xpath_av_by.AUDI,
                           model=xpath_av_by.AUDI_100)

    search = driver.find_element_by_xpath(xpath_av_by.SEARCH)
    search.click()

    assert driver.find_element_by_xpath(xpath_av_by.LISTING_TITLE)
    driver.quit()


def test_authorization():
    driver = authorization_setup(login='vlad.zver@tyt.by', password='135790qwe')

    assert driver.find_element_by_xpath(xpath_av_by.USER_BAR)
    driver.quit()


def test_authorization_wrong_login():
    driver = authorization_setup(login='vlad.zver@t', password='135790qwe')

    assert driver.find_element_by_xpath(xpath_av_by.ERROR_MESSAGE)
    driver.quit()


def test_authorization_wrong_password():
    driver = authorization_setup(login='vlad.zver@tyt.by', password='135790')

    assert driver.find_element_by_xpath(xpath_av_by.ERROR_MESSAGE)
    driver.quit()
