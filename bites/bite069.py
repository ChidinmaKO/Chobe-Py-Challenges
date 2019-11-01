import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    pattern = re.compile(r"[2]\d{3}\-\d{2}\-\w{5}\:\d{2}\:\d{2}")
    result = pattern.search(text)
    return True if result else False


def is_integer(number):
    """Return True if number is an integer"""
    pattern = r"^\-*?\d$"
    result = re.match(pattern, str(number))
    return True if result else False


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    pattern = re.compile(r"([\w]+\-[\w]+)")
    result = pattern.search(text)
    return True if result else False


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    pattern = r"\s*\([\w\.]+\)"
    sub_ = re.sub(pattern, "", text)
    return sub_


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    pattern = r"[\.,?:;!]\s*"
    split_ = re.split(pattern, text)
    result = list(filter(None, split_))
    return result


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    pattern = r"\s{2,}"
    sub_ = re.sub(pattern, " ", text)
    return sub_


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    pattern = re.compile(r"[aAeEiIoOuU]{3,}")
    match = pattern.search(word)
    return True if match else False


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    pattern = r"(\d{2})(\/)(\d{2})\2(\d{4})"
    new_format = r"\3\2\1\2\4"
    sub_ = re.sub(pattern, new_format, date)
    return sub_

# tests
from regex import (has_timestamp, is_integer,
                   has_word_with_dashes, remove_all_parenthesis_words,
                   split_string_on_punctuation, remove_duplicate_spacing,
                   has_three_consecutive_vowels,
                   convert_emea_date_to_amer_date)


def test_has_timestamp():
    assert has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.')
    assert has_timestamp('INFO 2014-06-01T13:28:51 Shutdown initiated.')
    assert not has_timestamp('INFO 2014-7-3T23:27:51 Shutdown initiated.')
    assert not has_timestamp('INFO 2014-07-03t23:27:1 Shutdown initiated.')


def test_is_integer():
    assert is_integer(1)
    assert is_integer(-1)
    assert not is_integer('str')
    assert not is_integer(1.1)


def test_has_word_with_dashes():
    assert has_word_with_dashes('this Bite is self-contained')
    assert has_word_with_dashes('the match ended in 1-1')
    assert not has_word_with_dashes('this Bite is not selfcontained')
    assert not has_word_with_dashes('the match ended in 1- 1')


def test_remove_all_parenthesis_words():
    input_string = 'good morning (afternoon), how are you?'
    expected = 'good morning, how are you?'
    assert remove_all_parenthesis_words(input_string) == expected
    input_string = 'math (8.6) and science (9.1) where his strengths'
    expected = 'math and science where his strengths'
    assert remove_all_parenthesis_words(input_string) == expected


def test_split_string_on_punctuation():
    input_string = 'hi, how are you doing? blabla'
    expected = ['hi', 'how are you doing', 'blabla']
    assert split_string_on_punctuation(input_string) == expected
    input_string = ';String. with. punctuation characters!'
    expected = ['String', 'with', 'punctuation characters']
    assert split_string_on_punctuation(input_string) == expected


def test_remove_duplicate_spacing():
    input_string = 'This is a   string with  too    much spacing'
    expected = 'This is a string with too much spacing'
    assert remove_duplicate_spacing(input_string) == expected


def test_has_three_consecutive_vowels():
    assert has_three_consecutive_vowels('beautiful')
    assert has_three_consecutive_vowels('queueing')
    assert not has_three_consecutive_vowels('mountain')
    assert not has_three_consecutive_vowels('house')


def test_convert_emea_date_to_amer_date():
    assert convert_emea_date_to_amer_date('31/03/2018') == '03/31/2018'
    assert convert_emea_date_to_amer_date('none') == 'none'