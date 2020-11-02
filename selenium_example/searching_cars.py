from selenium_example.XPATH import model_auto
from selenium_example.utilities import get_driver, select_brand, select_model, search, select_year


def search_auto(brand, model='Любая', year_from='с', year_to='по'):
    driver = get_driver('chrome')
    driver.get("https://av.by/")

    select_brand(driver, brand)
    select_model(driver, model_auto(model))
    select_year(driver, year_from, year_to)

    search(driver)
    return driver
