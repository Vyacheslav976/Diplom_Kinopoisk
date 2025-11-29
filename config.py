# UI  тесты
MAIN_URL = 'https://www.kinopoisk.ru/'
TITLE = ('Кинопоиск. Онлайн кинотеатр. '
         'Фильмы сериалы мультфильмы и энциклопедия')
SEARCH_TITLE = 'Кинопоиск — Все фильмы планеты'

# API  тесты
API_URL = 'https://api.kinopoisk.dev/'
API_KEY = '5N3TENX-YZSM43W-PKXPAPQ-ASCF5YG'

# Тестовые данные
VALID_UI_FILMS = [
    "ОНО 2",
    "Зеленая миля"
]
VALID_API_FILMS = [
    "Гарри Поттер",
    "The Green Mile",
    "1984"
]
VALID_MOVIE_ID = 350
INVALID_MOVIE_ID = 6
FILM_PAGE = "Интерстеллар"
FILM_PAGE_TITLE = 'Интерстеллар фильм, 2014, дата выхода трейлеры актеры отзывы описание на Кинопоиске'
EMPTY_QUERY = ""
INVALID_QUERY = "7+7"
SPECIAL_CHARS_QUERY = ":**(\"№%_)(*%!\"№_)*?:%%;!;%%:"
RUSSIAN_NO_SPACES = "Дартаньянитримушкетера"
FILM_PAGE_IDS = [889, 435, 326]