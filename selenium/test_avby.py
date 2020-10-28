from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_request_not_found():
    driver = webdriver.Firefox()
    driver.get("https://av.by/")
    driver.implicitly_wait(10)

    car_brand = driver.find_element_by_xpath('//option[@value=6]')
    car_brand.click()

    car_model = driver.find_element_by_xpath('//option[@value="10"]')
    car_model.click()

    produce_year = driver.find_element_by_xpath(
        '//div[@class="dropselect-head js-dropselect-head dropselect-head-year"]')
    produce_year.click()

    produce_year_from = driver.find_element_by_xpath('//select[@name="year_from"]/option[@value="2000"]')
    produce_year_from.click()

    search = driver.find_element_by_xpath('//button[@id="submit_presearch"]')
    search.click()

    assert "Мы не нашли объявлений по вашему запросу" in driver.page_source
    driver.close()


def test_request_found():
    driver = webdriver.Firefox()
    driver.get("https://av.by/")
    driver.implicitly_wait(10)

    car_brand = driver.find_element_by_xpath('//option[@value=6]')
    car_brand.click()

    car_model = driver.find_element_by_xpath('//option[@value="10"]')
    car_model.click()

    search = driver.find_element_by_xpath('//button[@id="submit_presearch"]')
    search.click()

    assert driver.find_element_by_xpath('//h3[@class="listing__title"]')
    driver.close()


def test_authorization():
    driver = webdriver.Firefox()
    driver.get("https://av.by/login/")
    driver.implicitly_wait(10)

    login = driver.find_element_by_xpath('//input[@id="login"]')
    login.send_keys('vlad.zver@tyt.by')

    password = driver.find_element_by_xpath('//input[@id="password"]')
    password.send_keys('135790qwe')
    password.send_keys(Keys.RETURN)

    assert driver.find_element_by_xpath('//li[@class="nav__item nav__item--dropdown nav__item--user"]')
    driver.close()


def test_authorization_wrong_login():
    driver = webdriver.Firefox()
    driver.get("https://av.by/login/")
    driver.implicitly_wait(10)

    login = driver.find_element_by_xpath('//input[@id="login"]')
    login.send_keys('vlad.zver@t')

    password = driver.find_element_by_xpath('//input[@id="password"]')
    password.send_keys('135790qwe')
    password.send_keys(Keys.RETURN)

    assert driver.find_element_by_xpath('//div[@class ="error-message"]')
    driver.close()


def test_authorization_wrong_password():
    driver = webdriver.Firefox()
    driver.get("https://av.by/login/")
    driver.implicitly_wait(10)

    login = driver.find_element_by_xpath('//input[@id="login"]')
    login.send_keys('vlad.zver@tyt.by')

    password = driver.find_element_by_xpath('//input[@id="password"]')
    password.send_keys('135790')
    password.send_keys(Keys.RETURN)

    assert driver.find_element_by_xpath('//div[@class ="error-message"]')
    driver.close()
