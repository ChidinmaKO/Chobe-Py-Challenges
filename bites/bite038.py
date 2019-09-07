# Bite 38. Using ElementTree to parse XML

import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree():
    """You probably want to use ET.fromstring"""
    root = ET.fromstring(xmlstring)
    return ET.ElementTree(root)


def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    tree = get_tree()
    movie_list = [movie.get("title") for movie in tree.getroot().findall("movie")]
    return movie_list


def get_movie_longest_runtime():
    """Call get_tree again and return the movie with the longest runtime in minutes,
       for latter consider adding a _get_runtime helper"""
    tree = get_tree()
    movie_runtimes = [(movie.get("title"), movie.get("runtime")) for movie in tree.getroot().findall("movie")]

    # one way
    result = sorted(movie_runtimes, key=lambda movie_runtimes: movie_runtimes[1], reverse = True)[0][0]
    return result
    
    # another way
    # result = max(movie_runtimes, key=lambda movie_runtimes: movie_runtimes[1])[0]
    # return result

# tests

# import xml.etree.ElementTree as ET

# from nolan import get_tree, get_movies, get_movie_longest_runtime


def test_get_tree():
    tree = get_tree()
    assert type(tree) in (ET.ElementTree, ET.Element)
    assert len(list(tree.iter(tag='movie'))) == 5


def test_get_movies():
    assert list(get_movies()) == ['The Prestige', 'The Dark Knight',
                                  'The Dark Knight Rises', 'Dunkirk',
                                  'Interstellar']


def test_get_movie_longest_runtime():
    assert get_movie_longest_runtime() == 'Interstellar'