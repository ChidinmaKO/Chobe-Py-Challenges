class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.new_max = 0
        
    def __call__(self, score):
        self.new_max = max(self.new_max, score)
        return self.new_max

    # another way
    # def __init__(self):
    #     self.scores = []
        
    # def __call__(self, new_scores):
    #     self.scores.append(new_scores)
    #     return max(self.scores)

# tests
import pytest

# from record import RecordScore


@pytest.fixture()
def record():
    """Make a RecordScore object with a few scores"""
    record = RecordScore()
    record(10)
    record(9)
    record(11)  # initial max
    record(5)
    return record


def test_record_unbeaten(record):
    assert record(9) == 11
    record(10)
    record(2)
    assert record(4) == 11


def test_record_got_beaten(record):
    assert record(4) == 11
    record(3)
    record(12)  # new record
    assert record(4) == 12
    record(5)
    record(16)  # another record
    assert record(4) == 16