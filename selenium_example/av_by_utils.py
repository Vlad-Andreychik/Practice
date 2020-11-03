from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from selenium_example import xpath as sxpath
from selenium_example.selenium_utils import wait_element
from selenium_example.xpath import get_model_auto


def search_auto(driver, brand, model='Любая', year_from='с', year_to='по'):
    select_brand(driver, brand)
    select_model(driver, get_model_auto(model))
    select_year(driver, year_from, year_to)

    search(driver)


def select_brand(driver, name):
    wait_element(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.get_brand(name)))).click()


def select_model(driver, model='Любая'):
    wait_element(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.get_model_auto(model)))).click()


def select_year(driver, year_from='с', year_to='по'):
    wait_element(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.PRODUCE_YEAR))).click()
    wait_element(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.get_year_from(year_from)))).click()
    wait_element(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.year_to(year_to)))).click()


def search(driver):
    wait_element(driver).until(ec.visibility_of_element_located((By.XPATH, sxpath.SEARCH))).click()