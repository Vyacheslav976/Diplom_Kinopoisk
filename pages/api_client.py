import requests
import allure
from config import API_URL, API_KEY


class APIClient:
    def __init__(self):
        self.base_url = API_URL.rstrip('/')
        self.headers = {'X-API-KEY': API_KEY} if API_KEY else {}

    @allure.step("Создание общего шаблона запроса")
    def request(self, method, endpoint, params=None, use_auth=True):
        """Создаёт шаблон запроса API"""
        url = f"{self.base_url}{endpoint}"
        headers = self.headers if use_auth else {}

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params
        )
        return response
# Поиск фильма по названию
    @allure.step("Поиск фильма по названию")
    def search_movies(self, query, page=1, limit=10, use_auth=True):
        """Создает запрос на поиск фильма по названию"""
        params = {'page': page, 'limit': limit, 'query': query}
        return self.request('GET', '/v1.4/movie/search', params, use_auth)
# Поиск фильма по ID
    @allure.step("Поиск фильма по ID")
    def get_movie_by_id(self, movie_id, use_auth=True):
        """Создает запрос на поиск фильма по его ID"""
        return self.request('GET', f'/v1.4/movie/{movie_id}', use_auth=use_auth)