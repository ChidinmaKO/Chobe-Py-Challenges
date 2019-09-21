import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    with requests.Session() as s:
        content = s.get(cached_so_url).content.decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        article = soup.find('div', {'id': 'questions'}).find_all('div', {'class': 'question-summary'})
        
        questions = []
        
        try:
            for summary in article:
                question = summary.select_one('.question-hyperlink').text.strip()
                votes = summary.select_one('.vote-count-post').text.strip()
                views = summary.select_one('.views').text.strip().replace(' views', '')
                
                if 'm' not in views:
                    continue
                questions.append((question, int(votes)))
                
                result = sorted(questions, key=lambda q: q[1], reverse=True)
        except Exception:
            pass
        else:
            return result


# tests

import pytest
# from so import top_python_questions

actual_return = top_python_questions()
expected_return = [
    ('What does the “yield” keyword do?', 9169),
    ('Does Python have a ternary conditional operator?', 5135),
    ('What does if __name__ == “__main__”: do?', 4927),
    ('Calling an external command in Python', 4190),
    ('How to merge two dictionaries in a single expression?', 3874),
    ('How do I sort a dictionary by value?', 3394),
    ('Using global variables in a function', 2768),
    ('Understanding slice notation', 2707),
    ('How to make a flat list out of list of lists', 2545),
    ('How do I install pip on Windows?', 2388),
    ('How do I pass a variable by reference?', 2295),
    ('How to clone or copy a list?', 2063),
    ('How to read a file line-by-line into a list?', 2000),
    ('Converting string into datetime', 1816),
    ('How to print without newline or space?', 1615),
    ('Select rows from a DataFrame based on '
     'values in a column in pandas', 1304),
    ("Why does comparing strings using either '==' or 'is' "
     'sometimes produce a different result?', 1008)
]


@pytest.mark.parametrize('actual, expected',
                         zip(actual_return, expected_return)
                         )
def test_top_python_questions(actual, expected):
    assert actual == expected