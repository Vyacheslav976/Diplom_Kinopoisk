import allure
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()
        self.close_communication_if_exists()

    def _wait_for_elements(self, by, value, multiple=False, timeout=10):
        if multiple:
            return WebDriverWait(
                self.driver, timeout).until(
                EC.visibility_of_all_elements_located(
                    (by, value)))
        else:
            return WebDriverWait(
                self.driver, timeout).until(
                EC.visibility_of_element_located(
                    (by, value)))

    def close_communication_if_exists(self, timeout=10):
        element = WebDriverWait(
            self.driver,
            timeout).until(
            EC.any_of(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     '[aria-label="Закрыть коммуникацию"]')),
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     '[name="kp_query"]'))))
        if element.get_attribute("aria-label") == "Закрыть коммуникацию":
            element.click()

    def _get_element_texts(self, css_selector):
        elements = self._wait_for_elements(
            By.CSS_SELECTOR, css_selector, multiple=True)
        return [element.text for element in elements]

    @allure.step("Получение заголовка страницы")
    def check_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.title != "")
        return self.driver.title == expected_title

    @allure.step("Поиск контента по фразе: {phrase}")
    def search_items_by_phrase(self, phrase):
        self._wait_for_elements(By.CSS_SELECTOR,
                                "input[name=kp_query]").send_keys(phrase)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[type=submit]").click()

    @allure.step("Получаем названия фильмов")
    def find_book_titles(self):
        return self._get_element_texts("[data-type='film']")

    @allure.step("Получаем количество результатов поиска")
    def get_search_results_count(self):
        results_text = self._wait_for_elements(
            By.CSS_SELECTOR, ".search_results_topText").text

        match = re.search(r'результаты:\s*(\d+)', results_text)
        if match:
            return int(match.group(1))
        else:
            return 0