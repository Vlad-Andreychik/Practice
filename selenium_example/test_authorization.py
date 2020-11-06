import selenium_example.xpath as xpath
from selenium_example.av_by_utils import authorization
from selenium_example.selenium_utils import wait_element


def test_correct_authorization(driver, setup_authorization):
    """
    Тест авторизации с корректным вводом данных
    """
    authorization(driver, 'vlad.zver@tyt.by', '135790qwe')
    assert wait_element(driver, xpath.USER_BAR).is_displayed()


def test_wrong_login(driver, setup_authorization):
    """
    Тест авторизации с неверным логином
    """
    authorization(driver, 'vlad.@tyt.by', '135790qwe')
    assert wait_element(driver, xpath.ERROR_MESSAGE).is_displayed()


def test_wrong_password(driver, setup_authorization):
    """
    Тест авторизации с неверным паролем
    """
    authorization(driver, 'vlad.zver@tyt.by', '1sda')
    assert driver.current_url == 'https://av.by/login'
