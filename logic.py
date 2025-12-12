import os
import json
from typing import List, Dict


def load_movies(path: str) -> List[Dict]:
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        
        return []


def save_movies(path: str, movies: List[Dict]) -> None:
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)


def add_movie(movies: List[Dict], title: str, year: int) -> List[Dict]:
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

    return movies + [new_movie]


def mark_watched(movies: List[Dict], movie_id: int) -> List[Dict]:
    
    updated_movies = []
    for movie in movies:
        movie_copy = dict(movie)  
        if movie_copy['id'] == movie_id:
            movie_copy['watched'] = True
        updated_movies.append(movie_copy)
    return updated_movies


def find_by_year(movies: List[Dict], year: int) -> List[Dict]:
    
    return [movie for movie in movies if movie['year'] == year]

