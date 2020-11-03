import selenium_example.xpath as xpath
from selenium_example.av_by_utils import search_auto
from selenium_example.selenium_utils import wait_element, get_driver, go_to_url

driver = get_driver('chrome')
go_to_url(driver)


def test_searching_cars_with_model():
    search_auto(driver, brand='Audi', model='TT')
    assert wait_element(driver, xpath.LISTING_TITLE)


def test_searching_cars_wrong_year_from():
    search_auto(driver, brand='Audi', model='100', year_from='2000')
    assert wait_element(driver, xpath.EMPTY_SEARCH)
