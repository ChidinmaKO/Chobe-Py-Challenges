import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    pattern = re.compile(r'\d{2}\:\d{2}')
    times = re.findall(pattern, course)
    return times


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    # one way
    # link_pattern = re.compile(r'https?://(?:[a-zA-Z0-9]|[$-_/.*]|(?:%[a-zA-Z0-9]+))+')
    # hashtag_pattern = re.compile(r'\B#\w*\b')
    
    # results = list()
    
    # for match_ in tweet.split(' '):
    #     if (link_pattern.match(match_)) or (hashtag_pattern.match(match_)):
    #         results.append(match_)
    # return results
    
    # another way
    pattern = re.compile(r'((?:#|https?)\S+)')
    result = re.findall(pattern, tweet)
    return result


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    pattern = re.compile(r'<p>(.*?)</p>')
    result = re.findall(pattern, html)
    return result[0]


# tests
from regex import (extract_course_times,
                   get_all_hashtags_and_links,
                   match_first_paragraph)


def test_extract_course_times_default_arg():
    expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
    assert extract_course_times() == expected


def test_extract_course_times_other_course_input():
    course = ('00:40 Lesson introduction'
              '01:33 Your 3 day overview'
              '08:12 Learning datetime and date'
              '06:07 Datetime timedelta usage'
              '04:02 Concepts: what did we learn')
    expected = ['00:40', '01:33', '08:12', '06:07', '04:02']
    assert extract_course_times(course) == expected


def test_get_all_hashtags_and_links_default_arg():
    expected = ['http://pybit.es/requests-cache.html', '#python', '#APIs']
    assert get_all_hashtags_and_links() == expected


def test_get_all_hashtags_and_links_other_tweet():
    tweet = ('PyBites My Reading List | 12 Rules for Life - #books '
             'that expand the mind! '
             'http://pbreadinglist.herokuapp.com/books/'
             'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'
             ' #psychology #philosophy')
    expected = ['#books',
                ('http://pbreadinglist.herokuapp.com/books/'
                 'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'),
                '#psychology', '#philosophy']
    assert get_all_hashtags_and_links(tweet) == expected


def test_match_first_paragraph_default_arg():
    expected = 'pybites != greedy'
    assert match_first_paragraph() == expected


def test_match_first_paragraph_other_html():
    html = ('<p>Match only this paragraph.</p>'
            '<p>Not this one!</p><p>And this one neither.</p>')
    expected = 'Match only this paragraph.'
    assert match_first_paragraph(html) == expected