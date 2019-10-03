import csv
from pathlib import Path
from urllib.request import urlretrieve
from typing import List
import re

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N:int =10, stats:Path =stats) -> List[int]:
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, 'r', encoding='utf-8-sig') as f:
        rows = csv.DictReader(f, delimiter=';')
        bite_list = []
        
        for row in rows:
            try:
                bite = row['Bite']
                difficulty = row['Difficulty']
            except ValueError:
                continue
            
            if 'None' in difficulty:
                continue
            else:
                bite_list.append((bite, difficulty))
                
        sorted_bite_list = sorted(bite_list, key=lambda bites: bites[1], reverse=True)
        
        result = []
        
        for bite in sorted_bite_list[:N]:
            bite_regex = re.search('^Bite (\d+)\.', bite[0])
            result.append(bite_regex.group(1))

        return result


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)

# tests

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

# from bites import get_most_complex_bites

TMP = Path('/tmp')
BITES_CSV = TMP / 'intro_bites.csv'
INTRO_BITE_STATS = """Bite;Difficulty
Bite 101. f-strings and a simple if/else;3.52
Bite 102. Infinite loop, input, continue and break;3.59
Bite 103. Loop through a dictionary and pluralise a word;3.21
Bite 104. Split and join;2.91
Bite 105. Slice and dice;5.0
Bite 106. Strip out vowels and count the number of replacements;4.73
Bite 107. Filter numbers with a list comprehension;1.89
Bite 108. Loop over a dict of namedtuples calculating a total score;4.83
Bite 109. Workout dict lookups and raising an exception;2.75
Bite 110. Type conversion and exception handling;1.5
"""


@pytest.fixture
def intro_bites():
    with TemporaryDirectory(dir=TMP):
        with open(BITES_CSV, 'w') as f:
            f.write(INTRO_BITE_STATS)
    return BITES_CSV


@pytest.mark.parametrize("N, expected", [
    (2, ['88', '31']),
    (6, ['88', '31', '50', '90', '179', '98']),
    (10, ['88', '31', '50', '90', '179', '98', '190', '42', '69', '40']),
])
def test_different_args_for_N(N, expected):
    actual = get_most_complex_bites(N)
    # str or int for IDs is fine with us
    actual = [str(i) for i in actual]
    assert actual == expected


@pytest.mark.parametrize("N, expected", [
    (1, ['105']),
    (3, ['105', '108', '106']),
    # res is max = size of bites in file:
    (15, ['105', '108', '106', '102', '101', '103',
          '104', '109', '107', '110']),
])
def test_only_intro_bites(intro_bites, N, expected):
    actual = get_most_complex_bites(N, stats=intro_bites)
    # str or int for IDs is fine with us
    actual = [str(i) for i in actual]
    assert actual == expected