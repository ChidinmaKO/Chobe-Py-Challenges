def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    
    # short way
    # word1 = word1.strip().replace(' ', '').lower()
    # word2 = word2.strip().replace(' ', '').lower()
    # return sorted(word1) == sorted(word2)
    
    # longer way
    word1 = word1.strip().replace(' ', '').lower()
    word2 = word2.strip().replace(' ', '').lower()
    
    if len(word1) != len(word2):
        return False
        
    count = {}
    
    for letter in word1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    for letter in word2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
            
    for c in count:
        if count[c] != 0:
            return False
    return True


# tests
# https://en.wikipedia.org/wiki/Anagram
# Anagrams may be created as a commentary on the subject.
# They may be a synonym or antonym of their subject,
# a parody, a criticism or satire.
import pytest

# from anagram import is_anagram


@pytest.mark.parametrize("word1, word2", [
    ("rail safety", "fairy tales"),
    ("roast beef", "eat for BSE"),
    # An anagram which means the opposite of its subject is
    # called an "antigram". For example:
    ("restful", "fluster"),
    ("funeral", "real fun"),
    ("adultery", "true lady"),
    ("customers", "store scum"),
    ("forty five", "over fifty"),
    # They can sometimes change from a proper noun or personal
    # name into an appropriate sentence:
    ("William Shakespeare", "I am a weakish speller"),
    ("Madam Curie", "Radium came"),
])
def test_is_anagram(word1, word2):
    assert is_anagram(word1, word2)


@pytest.mark.parametrize("word1, word2", [
    ("rail safety", "fairy fun"),
    ("roast beef", "eat for ME"),
    ("restful", "fluester"),
    ("funeral", "real funny"),
    ("adultery", "true ladie"),
    ("customers", "store scam"),
    ("forty five", "over fifty1"),
    ("William Shakespeare", "I am a strong speller"),
    ("Madam Curie", "Radium come"),
])
def test_is_not_anagram(word1, word2):
    assert not is_anagram(word1, word2)