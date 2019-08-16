import os
import urllib.request
import re
import string
import collections

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with open(harry_text, 'r') as rharry, open(stopwords_file, 'r') as rstop:
        # replace stopwords & non-alphanumeric characters with ''
        text = re.sub(f"[{string.punctuation}]", "", rharry.read().lower()).split()
        stopwords = set(rstop.read().lower().split('\n'))
    count = collections.Counter(text)
    result = [count.pop(t) for t in stopwords if t in count]
    return count.most_common(1)[0]
    

# tests
from harry import get_harry_most_common_word


def test_get_harry_most_common_word():
    top_word = get_harry_most_common_word()
    assert type(top_word) == tuple
    assert top_word[0] == 'dursley'
    assert top_word[1] == 45