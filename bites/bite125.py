from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
TIM_BLOG = 'https://bit.ly/2NBnZ6P'


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content, 'html.parser')
    article = soup.find('div', class_='entry-content')
    links = article.find_all('a')
    
    try:
        books = [a.get_text() for a in links if AMAZON in a.get('href').lower()]
        count = Counter(books)
        top_limit_books = [book[0] for book in count.most_common(limit)]
    except Exception:
        pass
    else:
        return top_limit_books
# tests
# from tribe import load_page, get_top_books

content = load_page()  # make sure we do this once!
books = get_top_books(content=content)


def test_books_6_occurrences():
    assert books[0] == 'Man’s Search For Meaning'


def test_books_5_occurrences():
    assert books[1] == 'Tao Te Ching'


def test_books_4_occurrences():
    assert sorted(books[2:5]) == ['Sapiens: A Brief History of Humankind',
                                  ('The 4-Hour Workweek: Escape the 9-5, Live '
                                   'Anywhere and Join the New Rich'),
                                  'The Fountainhead']  # 4x