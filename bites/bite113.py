def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return list(t for t in text.split() if not t.isascii())


# another way
def _is_ascii(word):
    """Helper to determine if a word consists of only ascii chars"""
    return not all(ord(char) < 128 for char in word)


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split() if _is_ascii(word)]

# tests
import pytest

from non_ascii import extract_non_ascii_words


@pytest.mark.parametrize("phrase, expected", [
    ('An preost wes on leoden, Laȝamon was ihoten', ['Laȝamon']),
    ('He wes Leovenaðes sone -- liðe him be Drihten', ['Leovenaðes', 'liðe']),
    ('He wonede at Ernleȝe at æðelen are chirechen', ['Ernleȝe', 'æðelen']),
    ('Uppen Sevarne staþe, sel þar him þuhte', ['staþe,', 'þar', 'þuhte']),
    ('Onfest Radestone, þer he bock radde', ['þer']),
    ('Fichier non trouvé', ['trouvé']),
    ('Over \u0e55\u0e57 57 flavours', ['๕๗']),
    ('Sí ... habrá que saber algo de Unicode, ¿no?', ['Sí', 'habrá', '¿no?']),
    ('This string only contains ascii words', []),
])
def test_extract_non_ascii_words(phrase, expected):
    assert extract_non_ascii_words(phrase) == expected