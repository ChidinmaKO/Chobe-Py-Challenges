from csv import DictReader
from os import path
from urllib.request import urlretrieve
from collections import Counter

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        # rows = []
        # with open(data) as csv_file:
        #     dict_data = DictReader(csv_file)
        #     for row in dict_data:
        #         rows.append(row)
        # ---------------------------------------
        rows = list(DictReader(open(data)))
        return rows

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        unique_bites = len({row['bite'] for row in self.rows})
        return unique_bites

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        resolved_bites = len({row['bite'] for row in self.rows if row['completed'] == 'True'})
        return resolved_bites

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        active_users = len({row['user'] for row in self.rows})
        return active_users

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        user_bites = [row['user'] for row in self.rows if row['completed'] == 'True']
        count = len(Counter(user_bites).most_common())
        return count

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        bites = [row['bite'] for row in self.rows]
        most_accessed_bite = Counter(bites).most_common()[0][0]
        return most_accessed_bite

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        user_bites = [row['user'] for row in self.rows if row['completed'] == 'True']
        top_user = Counter(user_bites).most_common()[0][0]
        return top_user



# tests 
import pytest

from stats import BiteStats


@pytest.fixture(scope="module")
def bite_stats():
    return BiteStats()


def test_number_bites_accessed(bite_stats):
    assert bite_stats.number_bites_accessed == 176


def test_number_bites_resolved(bite_stats):
    assert bite_stats.number_bites_resolved == 115


def test_number_users_active(bite_stats):
    assert bite_stats.number_users_active == 114


def test_number_users_solving_bites(bite_stats):
    assert bite_stats.number_users_solving_bites == 76


def test_top_bite_by_number_of_clicks(bite_stats):
    assert int(bite_stats.top_bite_by_number_of_clicks) == 101


def test_top_user_by_bites_completed(bite_stats):
    assert bite_stats.top_user_by_bites_completed == 'mcaberasu'