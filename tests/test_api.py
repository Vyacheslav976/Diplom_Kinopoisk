import pytest
import allure
from config import *


@allure.story("API")
@allure.title("Поиск фильма по валидному названию")
@pytest.mark.parametrize("query", VALID_API_FILMS)
@pytest.mark.api
@pytest.mark.positive
def test_search_valid_queries(client, query):
    response = client.search_movies(query)

    assert response.status_code == 200
    data = response.json()
    assert "docs" in data
    assert isinstance(
        data["docs"], list), f"Ожидался список list, но получен {
        type(
            data["docs"])}"


@allure.story("API")
@allure.title("Поиск по валидному ID")
@pytest.mark.api
@pytest.mark.positive
def test_get_movie_by_id(client):
    response = client.get_movie_by_id(VALID_MOVIE_ID)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == VALID_MOVIE_ID, f" ID - {VALID_MOVIE_ID} не является валидным значением"
    assert "name" in data


@allure.story("API")
@allure.title("Пустой поиcк")
@pytest.mark.api
@pytest.mark.negative
def test_empty_query(client):
    response = client.search_movies(EMPTY_QUERY)
    assert response.status_code == 200


@allure.story("API")
@allure.title("Поиск по невалидному названию")
@pytest.mark.api
@pytest.mark.negative
def test_invalid_query(client):
    response = client.search_movies(INVALID_QUERY)
    assert response.status_code == 200
    data = response.json()
    assert len(data.get("docs", [])) == 0


@allure.story("API")
@allure.title("Поиск в названии спецсимволы")
@pytest.mark.api
@pytest.mark.negative
def test_special_chars_query(client):
    response = client.search_movies(SPECIAL_CHARS_QUERY)
    assert response.status_code == 200


@allure.story("API")
@allure.title("Поиск по названию без пробелов")
@pytest.mark.api
@pytest.mark.negative
def test_russian_no_spaces(client):
    response = client.search_movies(RUSSIAN_NO_SPACES)
    assert response.status_code == 200
    assert len(response.json().get("docs", [])) == 0


@allure.story("API")
@allure.title("Поиск без token")
@pytest.mark.api
@pytest.mark.negative
def test_without_token(client):
    response = client.get_movie_by_id(INVALID_MOVIE_ID, use_auth=False)
    assert response.status_code == 401
