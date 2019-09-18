from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

# import lxml

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT)
    book = soup.find('div', class_="dotd-main-book cf")
    inner = book.findChild('div', class_="section-inner")
    section = (inner.findChildren('div'))
    
    book_title = section[3].h2.text.strip()
    
    description = section[3].findNext("div").text.strip()
    
    image = section[0].find('img', class_="bookimage imagecache imagecache-dotd_main_image")["src"]
    
    link = section[0].a['href']
    
    book_tuple = Book(book_title, description, image, link)
    return book_tuple

# tests

# from packt import get_book

book = get_book()


def test_type():
    assert isinstance(book, tuple)


def test_book_title():
    assert book.title == 'Mastering TypeScript - Second Edition'


def test_book_description():
    assert book.description == ('Build enterprise-ready, industrial-strength '
                                'web applications using '
                                'TypeScript and leading JavaScript frameworks')


def test_book_image():
    assert book.image == '//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/B05588.png'  # noqa E501


def test_book_link():
    assert book.link == '/application-development/mastering-typescript-second-edition'  # noqa E501