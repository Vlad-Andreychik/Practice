import pytest

from selenium_example.selenium_utils import get_driver, go_to_url_main, go_to_url_login


@pytest.fixture()
def setup_search(driver):
    """
    Фикстура переходит по url-адресу на главную страницу, проводит тест и закрывает браузер.
    """
    go_to_url_main(driver)
    yield
    driver.quit()


@pytest.fixture()
def setup_authorization(driver):
    """
    Фикстура переходит по url-адресу на страницу авторизации, проводит тест и закрывает браузер.
    """
    go_to_url_login(driver)
    yield
    driver.quit()


@pytest.fixture()
def driver():
    """
    Фикстура создания драйвера.
    """
    driver = get_driver('chrome')
    return driver

# TODO[agorozhanko 06.11.2020]: где пустая строка в конце файла?
# TODO[vandreychyk 06.11.2020]: добавил
