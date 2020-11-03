from selenium_example.selenium_utils import select_brand, select_model, search, select_year
from selenium_example.xpath import get_model_auto


def search_auto(driver, brand, model='Любая', year_from='с', year_to='по'):
    select_brand(driver, brand)
    select_model(driver, get_model_auto(model))
    select_year(driver, year_from, year_to)

    search(driver)
