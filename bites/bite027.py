import glob
import json
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movie_list = []
    for file in files:
        with open(file, 'r') as data:
            movie_data = json.loads(data.read())
            movie_list.append(movie_data)
    return movie_list


def get_single_comedy(movies):
    single_comedy = [movie['Title'] for movie in movies if 'Comedy' in movie['Genre']]
    single_comedy = ''.join(map(str, single_comedy))
    return single_comedy


def get_movie_most_nominations(movies):
    most_nominations = max(movies, key=lambda movie: int(movie['Awards'].split()[-2]))['Title']
    return most_nominations


def get_movie_longest_runtime(movies):
    longest_runtime = max(movies, key=lambda movie: int(movie['Runtime'].split()[0]))['Title']
    return longest_runtime


# tests
from omdb import (get_movie_data, get_single_comedy,
                  get_movie_most_nominations, get_movie_longest_runtime)

movies = get_movie_data()


def test_movie_data_structure():
    assert len(movies) == 5
    assert all(type(m) == dict for m in movies)


def test_data_analysis():
    assert get_single_comedy(movies) == 'Horrible Bosses'
    assert get_movie_most_nominations(movies) == 'Fight Club'
    assert get_movie_longest_runtime(movies) == 'Blade Runner 2049'