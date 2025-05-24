'''
Some tests
Run them with pytest tests.py
'''

from random import choice
from solution import refactor_data, top_10_movies, TOP_MOVIES

MOVIES_LIST = [
    [1, 9.0, 'Interstellar', True],
    [2, 8.5, 'Fast and the Furious', True],
    [3, 7.8, 'The Midnight Sky', False],
    [4, 9.2, 'The Shawshank Redemption', True],
    [5, 8.1, 'Jurassic Park', True],
    [6, 6.5, 'Morbius', False],
    [7, 9.0, 'The Godfather', True],
    [8, 8.8, 'Pulp Fiction', True],
    [9, 7.2, 'Eternals', False],
    [10, 9.5, 'The Dark Knight', True],
    [11, 8.3, 'Inception', True],
    [12, 6.9, 'Transformers: The Last Knight', False],
    [13, 8.7, 'Forrest Gump', True],
    [14, 8.0, 'The Matrix', True],
    [15, 7.5, 'Wonder Woman 1984', False],
    [16, 9.1, "Schindler's List", True],
    [17, 8.6, 'The Lord of the Rings: The Return of the King', True],
    [18, 7.0, 'Suicide Squad (2016)', False],
    [19, 8.9, 'Fight Club', True],
    [20, 8.2, 'Gladiator', True],
    [21, 6.7, 'Cats', False],
    [22, 9.3, 'The Lord of the Rings: The Fellowship of the Ring', True],
    [23, 8.4, 'Saving Private Ryan', True],
    [24, 7.9, 'Black Adam', False],
    [25, 8.8, 'The Green Mile', True],
    [26, 7.7, 'Avatar: The Way of Water', True],
    [27, 6.2, 'The Emoji Movie', False],
    [28, 9.0, 'Star Wars: Episode V - The Empire Strikes Back', True],
    [29, 8.5, 'Back to the Future', True],
    [30, 7.3, 'Justice League (2017)', False],
    [31, 8.7, 'The Silence of the Lambs', True],
    [32, 8.1, 'Braveheart', True],
    [33, 6.8, 'Ghostbusters (2016)', False],
    [34, 9.2, 'The Good, the Bad and the Ugly', True],
    [35, 8.6, 'Spirited Away', True],
    [36, 7.1, 'The Mummy (2017)', False],
    [37, 8.9, 'Parasite', True],
    [38, 8.0, 'Mad Max: Fury Road', True],
    [39, 6.4, 'Movie 43', False],
    [40, 9.4, 'The Intouchables', True]
]

def test_refactor_data():
    formated_data = refactor_data(MOVIES_LIST)
    some_movie = choice(formated_data)
    assert type(formated_data) == list
    assert type(some_movie) == dict

def test_top_10_movies():
    refactored_list = refactor_data(MOVIES_LIST)
    top = top_10_movies(refactored_list)
    assert len(top) == TOP_MOVIES
    assert top[0]['rating'] == 9.5
    assert top[0]['certified_fresh']
    assert all([item['certified_fresh'] for item in top])
