import pytest

import selenium_example.xpath as xpath
from selenium_example.av_by_utils import search_auto
from selenium_example.selenium_utils import wait_element, get_driver, go_to_url

driver = get_driver('chrome')
go_to_url(driver)


@pytest.fixture()
def closing_browser():
    """
    Фикстура закрывает браузер после выполнения всех тестов в данном модуле
    """
    yield
    driver.quit()


@pytest.fixture()
def back_page():
    """
    Фикстура возвращает предыдущую страницу и обновляет ее после выполнения теста, который использует ее
    """
    yield
    driver.back()
    driver.refresh()


def test_searching_cars_with_model(back_page):
    """
    Тест поиска авто с корректным вводом данных
    """
    search_auto(driver, brand='Audi', model='TT')
    listing_container = wait_element(driver, xpath.LISTING_CONTAINER)
    listing_items = listing_container.find_elements_by_xpath(xpath.LISTING_ITEMS)
    assert len(listing_items) > 0


def test_searching_cars_wrong_year_from(closing_browser):
    """
    Тест поиска авто с некорректным вводом данных(несуществующий год выпуска для данной модели марки)
    """
    search_auto(driver, brand='Audi', model='100', year_from='2000')
    assert wait_element(driver, xpath.EMPTY_SEARCH)
