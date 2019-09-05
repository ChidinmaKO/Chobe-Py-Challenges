import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    with open(local, 'r') as f:
        movie_rows = csv.DictReader(f)
        
        movie_list = defaultdict(list)
        for movie in movie_rows:
            try:
                director = movie['director_name']
                title = movie['movie_title'].strip()
                year = int(movie['title_year'])
                score = float(movie['imdb_score'])
            except ValueError:
                continue
            
            if year and year < MIN_YEAR:
                continue
            else:
                movie_tuple = Movie(title, year, score)
                movie_list[director].append(movie_tuple)
        return movie_list


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    
    movie_list = [movie.score for movie in movies]
    result = sum(movie_list) / len(movie_list)
    return round(result, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    result = [(director, calc_mean_score(movies)) for director, movies in directors.items() if len(movies) >= MIN_MOVIES]
    return sorted(result, key=lambda result: result[1], reverse=True)

# tests
# from collections import defaultdict
# from directors import (get_movies_by_director, get_average_scores, calc_mean_score, Movie)

director_movies = get_movies_by_director()


def test_get_movies_by_director():
    assert 'Sergio Leone' in director_movies
    assert len(director_movies['Sergio Leone']) == 4
    assert len(director_movies['Peter Jackson']) == 12


def test_director_movies_data_structure():
    assert type(director_movies) in (dict, defaultdict)
    assert type(director_movies['Peter Jackson']) == list
    assert type(director_movies['Peter Jackson'][0]) == Movie


def test_calc_mean_score():
    movies_sergio = director_movies['Sergio Leone']
    movies_nolan = director_movies['Christopher Nolan']
    assert calc_mean_score(movies_sergio) == 8.5
    assert calc_mean_score(movies_nolan) == 8.4


def test_get_average_scores():
    # top 2
    scores = get_average_scores(director_movies)

    assert scores[0] == ('Sergio Leone', 8.5)
    assert scores[1] == ('Christopher Nolan', 8.4)

    # order / score might slightly change depending the way the mean
    # is calculated so only test director names in top scores
    directors = {score[0] for score in scores[2:13]}

    assert 'Quentin Tarantino' in directors
    assert 'Hayao Miyazaki' in directors
    assert 'Frank Darabont' in directors
    assert 'Stanley Kubrick' in directors
    assert 'James Cameron' in directors
    assert 'Joss Whedon' in directors
    assert 'Alejandro G. Iñárritu' in directors