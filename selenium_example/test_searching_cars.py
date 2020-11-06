import selenium_example.xpath as xpath
from selenium_example.av_by_utils import search_auto
from selenium_example.selenium_utils import wait_element


# TODO[agorozhanko 05.11.2020]:где запуск браузера перед каждым тестом и закрытие после?

# TODO[agorozhanko 06.11.2020]:код не запускается, снова

# TODO[agorozhanko 06.11.2020]:где тесты логина?
def test_searching_cars_with_model(setup, driver):
    """
    Тест поиска авто с корректным вводом данных
    """
    search_auto(driver, brand='Audi', model='TT')
    listing_container = wait_element(driver, xpath.LISTING_CONTAINER)
    listing_items = listing_container.find_elements_by_xpath(xpath.LISTING_ITEMS)
    assert len(listing_items) > 0


def test_searching_cars_wrong_year_from(setup, driver):
    """
    Тест поиска авто с некорректным вводом данных(несуществующий год выпуска для данной модели марки)
    """
    search_auto(driver, brand='Audi', model='100', year_from='2000')
    element = wait_element(driver, xpath.EMPTY_SEARCH)
    assert element.text == "Мы не нашли объявлений по вашему запросу"
