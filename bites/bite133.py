import re

def generate_affiliation_link(url):
    # result = f"http://www.amazon.com/dp/{url.split('/')[5]}"
    # tag = '/?tag=pyb0f-20'
    # return result + tag
    
    # with regex although it's an overkill
    pattern = re.compile(r'https?:\/+(www\.)?(\w+)(\.\w+)*(\S+)(\/dp\/)(\d+\w?)(\/*\S+)?')
    first = 'http://www.'
    tag = '/?tag=pyb0f-20'
    com = '.com'
    sub1 = pattern.sub(r'\2', url)
    sub2 = pattern.sub(r'\5\6', url)
    result = first + sub1 + com + sub2 + tag
    return result

# tests
import pytest

from affiliation import generate_affiliation_link

original_links = [
    'https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art',
    'https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1',
    'https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234',
    'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
    'https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/',
]
result_links = [
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20',
    'http://www.amazon.com/dp/020161622X/?tag=pyb0f-20',
    'http://www.amazon.com/dp/1449340377/?tag=pyb0f-20',
]


@pytest.mark.parametrize('amz_link, affil_link', zip(original_links,
                                                     result_links))
def test_get_word_max_vowels(amz_link, affil_link):
    assert generate_affiliation_link(amz_link) == affil_link