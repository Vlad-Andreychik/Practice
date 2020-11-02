from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium_example.XPATH import ImmutableXpath
from selenium_example.searching_cars import search_auto
from selenium_example.utilities import wait


def test_searching_cars_wrong_year_from():
    assert wait(search_auto('Audi', '100', year_from='2000')).until(
        EC.visibility_of_element_located((By.XPATH, ImmutableXpath.ERROR_MESSAGE)))


def test_searching_cars_with_model():
    assert wait(search_auto('Audi', 'TT')).until(
        EC.visibility_of_element_located((By.XPATH, ImmutableXpath.LISTING_TITLE)))
