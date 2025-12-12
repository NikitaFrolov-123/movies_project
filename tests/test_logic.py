import json
import os
import pytest
from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year



def test_load_movies_file_not_found(tmp_path):
    fake_path = tmp_path / "non_existent_file.json"
    result = load_movies(str(fake_path))
    assert result == []


def test_load_movies_invalid_json(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{corrupted data...", encoding="utf-8")

    result = load_movies(str(p))
    assert result == []


def test_load_movies_valid_data(tmp_path):
    p = tmp_path / "movies.json"
    data = [{"id": 1, "title": "Test Movie", "year": 2020, "watched": False}]
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f)

    result = load_movies(str(p))
    assert result == data
    assert len(result) == 1
    assert result[0]["title"] == "Test Movie"



def test_save_movies(tmp_path):
    p = tmp_path / "saved_movies.json"
    movies = [
        {"id": 1, "title": "Avatar", "year": 2009, "watched": True},
        {"id": 2, "title": "Titanic", "year": 1997, "watched": False}
    ]

    save_movies(str(p), movies)

    assert os.path.exists(p)

    with open(p, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)

    assert loaded_data == movies



def test_add_movie_to_empty_list():
    movies = []
    updated_movies = add_movie(movies, "Matrix", 1999)

    assert len(updated_movies) == 1
    assert updated_movies[0]["id"] == 1
    assert updated_movies[0]["title"] == "Matrix"
    assert updated_movies[0]["year"] == 1999
    assert updated_movies[0]["watched"] is False


def test_add_movie_increments_id():
    movies = [
        {"id": 10, "title": "Old Movie", "year": 1990, "watched": True}
    ]
    updated_movies = add_movie(movies, "New Movie", 2023)

    assert len(updated_movies) == 2
    assert updated_movies[1]["id"] == 11
    assert updated_movies[1]["title"] == "New Movie"



def test_mark_watched_existing_id():
    movies = [
        {"id": 1, "title": "A", "year": 2000, "watched": False},
        {"id": 2, "title": "B", "year": 2000, "watched": False}
    ]

    updated_movies = mark_watched(movies, 2)

    assert updated_movies[0]["watched"] is False
    assert updated_movies[1]["id"] == 2
    assert updated_movies[1]["watched"] is True
