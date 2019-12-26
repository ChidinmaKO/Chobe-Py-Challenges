import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return 'Not found'


def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    emojis = {}
    for i in range(START_EMOJI_RANGE, sys.maxunicode + 1):
        try:
            emojis[chr(i)] = unicodedata.name(chr(i)).lower()
        except ValueError:
            pass
    return emojis


def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()

    emoji_mapping = _make_emoji_mapping()

    # ... your turn ...

    for emoji, name in emoji_mapping.items():
        if term in name:
            print(f"{name:40} | {emoji}")
    else:
        print("no matches")

# tests
from emoji import what_means_emoji, find_emoji


def test_what_means_emoji_found():
    what_means_emoji('🐶').lower() == 'dog face'
    what_means_emoji('🏋').lower() == 'weight lifter'
    what_means_emoji('🌇').lower() == 'sunset over buildings'


def test_what_means_emoji_not_found():
    assert what_means_emoji('aaa').lower() == 'not found'


def test_find_matches(capfd):
    find_emoji('sun')
    output = capfd.readouterr()[0].lower()
    # some of the results you should get back
    assert 'sunrise' in output
    assert '🌅' in output
    assert 'sunset over buildings' in output
    assert '🌇' in output
    assert 'sun with face' in output
    assert '🌻' in output


def test_find_no_match(capfd):
    find_emoji('awesome')
    output = capfd.readouterr()[0].lower()
    assert not output.strip() or 'no matches' in output.lower()