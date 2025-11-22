import pytest
import allure
from pages.main_page import MainPage
from selenium import webdriver
from config import MAIN_URL, TITLE


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get(MAIN_URL)
    driver.get(MAIN_URL)
    return MainPage(driver, MAIN_URL)


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(TITLE)


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию")
@pytest.mark.parametrize("film_title",
                         ["Аватар", "Такси 4"])
def test_search_book_by_title(main_page, film_title):
    with allure.step(f"Поиск фильмов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название фильма {film_title} содержится в результатах"):
        assert film_title in main_page.find_book_titles()