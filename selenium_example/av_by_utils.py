from selenium_example import selenium_utils as su
from selenium_example import xpath as sxpath


def search_auto(driver, brand, model='Любая', year_from='с', year_to='по'):
    select_brand(driver, brand)
    select_model(driver, sxpath.get_model_auto(model))
    select_year(driver, year_from, year_to)

    search(driver)


def select_brand(driver, name):
    su.click_element(driver, sxpath.get_brand(name))


def select_model(driver, model='Любая'):
    su.click_element(driver, sxpath.get_model_auto(model))


def select_year(driver, year_from='с', year_to='по'):
    su.click_element(driver, sxpath.get_model_auto(sxpath.PRODUCE_YEAR))
    su.click_element(driver, sxpath.get_model_auto(sxpath.get_year_from(year_from)))
    su.click_element(driver, sxpath.get_model_auto(sxpath.year_to(year_to)))


def search(driver):
    su.click_element(driver, sxpath.get_model_auto(sxpath.SEARCH))
