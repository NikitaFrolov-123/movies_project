import os
import json
from typing import List, Dict


def load_movies(path: str) -> List[Dict]:
    """Загрузка списка фильмов из JSON-файла."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Убедимся, что содержимое — это список
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файл не существует или повреждён — возвращаем пустой список
        return []


def save_movies(path: str, movies: List[Dict]) -> None:
    """Сохранение списка фильмов в JSON-файл."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)


def add_movie(movies: List[Dict], title: str, year: int) -> List[Dict]:
    """Добавление нового фильма в список."""
    # Определяем новый ID
    if movies:
        new_id = max(movie['id'] for movie in movies) + 1
    else:
        new_id = 1

    new_movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False
    }

    # Возвращаем новый список (не мутируем входной)
    return movies + [new_movie]


def mark_watched(movies: List[Dict], movie_id: int) -> List[Dict]:
    """Отметить фильм как просмотренный."""
    # Создаём копию списка и словарей, чтобы не изменять исходные данные
    updated_movies = []
    for movie in movies:
        movie_copy = dict(movie)  # поверхностная копия словаря
        if movie_copy['id'] == movie_id:
            movie_copy['watched'] = True
        updated_movies.append(movie_copy)
    return updated_movies


def find_by_year(movies: List[Dict], year: int) -> List[Dict]:
    """Поиск всех фильмов указанного года."""
    return [movie for movie in movies if movie['year'] == year]


# import json
# import os
#
#
# import json
# from typing import List, Dict, Any


# def load_movies(path: str) -> List[Dict[str, Any]]:
#     """Загружает список фильмов из JSON-файла. Возвращает пустой список при ошибках."""
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#             if isinstance(data, list):
#                 return data
#             else:
#                 return []
#     except (FileNotFoundError, json.JSONDecodeError, IOError):
#         return []
#

# def save_movies(path: str, movies: List[Dict[str, Any]]) -> None:
#     """Сохраняет список фильмов в JSON-файл."""
#     pass
#
#
# def add_movie(movies: List[Dict[str, Any]], title: str, year: int) -> List[Dict[str, Any]]:
#     """Добавляет новый фильм в список и возвращает обновлённую копию."""
#     pass
#
#
# def mark_watched(movies: List[Dict[str, Any]], movie_id: int) -> List[Dict[str, Any]]:
#     """Отмечает фильм с указанным ID как просмотренный. Возвращает обновлённый список."""
#     pass
#
#
# def find_by_year(movies: List[Dict[str, Any]], year: int) -> List[Dict[str, Any]]:
#     """Возвращает список фильмов, выпущенных в указанном году."""
#     pass
