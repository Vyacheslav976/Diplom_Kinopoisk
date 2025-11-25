import pytest
import allure
from pages.ui_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import MAIN_URL, TITLE


@pytest.fixture
def driver():
    """Фикстура для создания драйвера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    """Фикстура для создания главной страницы"""
    driver.get(MAIN_URL)
    driver.get(MAIN_URL)
    return MainPage(driver, MAIN_URL)


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    """Smoke тест проверки заголовка главной страницы"""
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(TITLE)


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию")
@pytest.mark.parametrize("film_title",
                         ["Интерстеллар", "Начало", "Матрица"])
def test_search_film_by_title(main_page, film_title):
    """Тест поиска фильма по названию на главной странице"""
    with allure.step(f"Поиск фильмов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Проверяет, что количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0, 'Не удалось получить список фильмов'
    with allure.step(f"Получение списка найденных фильмов"):
        assert film_title in main_page.find_films_titles(), "Фильм не найден в результатах поиска"
        # film_titles = main_page.find_films_titles()
        # assert len(film_titles) > 0, "Не удалось получить список фильмов"

@allure.feature("Выбор")
@allure.story("UI")
@allure.title("Выбор фильма и просмотр")
@pytest.mark.parametrize("film_title", ["Интерстеллар"])
def test_choosing_and_watching_movie(main_page, film_title):
    """Тест выбора и просмотра фильма через поиск на главной странице"""
    main_page.search_items_by_phrase(film_title)
    assert main_page.check_page_title(f"Результаты поиска - Кинопоиск"),\
        "Не удалось перейти на страницу результатов поиска"
    assert main_page.get_search_results_count() > 0, f"По запросу не найдено ни одного результата"
    film_titles = main_page.find_films_titles()
    # assert len(film_titles) > 0, "Не удалось получить список фильмов"

    with allure.step("Возвращает TRUE, если хотя бы один элемент в генераторе равен TRUE"):
        film_found = any(film_title.lower() == title.lower() for title in film_titles)
        assert film_found, "Фильм не найден в результатах поиска"
        main_page._wait_for_elements(By.CSS_SELECTOR, "[data-type='film']").click()
        main_page._wait_for_elements(By.XPATH,"//button[contains(text(),"
                                                        " 'Смотреть') or contains(text(), 'Трейлер')]").click()

@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Написание рецензии к фильму")
@pytest.mark.smoke
def test_writing_movie_review(main_page, film_title):
    """"Тест написания рецензии на фильм"""
    with allure.step(f"Поиск фильма по названию {film_title}"):
        main_page.search_items_by_phrase(film_title)
    assert main_page.check_page_title(f"Результаты поиска - Кинопоиск"), \
        "Не удалось перейти на страницу результатов поиска"
    # Кликаем на первый фильм в результатах поиска
    main_page._wait_for_elements(By.CSS_SELECTOR, "[data-type='film']").click()
    # Ждем загрузки страницы фильма
    main_page._wait_for_elements(By.CSS_SELECTOR, "[data-test-id='film-page']").click()
    # Прокручиваем до раздела рецензий
    reviews_button = main_page.driver