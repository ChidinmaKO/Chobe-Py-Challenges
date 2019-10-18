import os
from collections import Counter
import urllib.request
import re

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    pattern = re.compile(r"<category>(\w*)</category>")
    tags = re.findall(pattern, content)
    count_n = Counter(tags).most_common(n)
    return count_n

# tests
from tags import get_pybites_top_tags


def test_get_pybites_top_tags():
    expected = [('python', 79),
                ('learning', 79),
                ('codechallenges', 72),
                ('twitter', 62),
                ('tips', 61),
                ('flask', 52),
                ('news', 49),
                ('django', 37),
                ('code', 25),
                ('github', 24)]
    assert get_pybites_top_tags() == expected