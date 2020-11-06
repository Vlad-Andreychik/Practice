import pytest

from selenium_example.selenium_utils import get_driver

driver = get_driver('chrome')


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
    driver.refresh() # TODO[agorozhanko 06.11.2020]: где пустая строка в конце файла?