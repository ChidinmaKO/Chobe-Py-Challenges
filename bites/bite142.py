from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    total_scores = 0
    
    for score in scores:
        if score not in DICE_VALUES:
            raise ValueError("Invalid data sis!")
        if score >= MIN_SCORE:
            total_scores += score
    return total_scores


def get_winner(players):
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    
    scores = []
    len_score = []
    for player in players:
        scores.append((player, calculate_score(player.scores)))
        len_score.append(len(player.scores))
        #  ensure that the length of scores matches
        if min(len_score) != max(len_score):
            raise ValueError("something fishy about the length of scores!")
    
        result = sorted(scores, key=lambda x: x[1], reverse=True)[0][0]
    return result



# tests

import pytest

from scores import Player, calculate_score, get_winner


def test_calculate_score():
    assert calculate_score([1, 3, 2, 5]) == 5
    assert calculate_score([1, 4, 2, 5]) == 9
    assert calculate_score([1, 1, 1, 1]) == 0
    assert calculate_score([4, 5, 1, 2]) == 9
    assert calculate_score([6, 6, 5, 5]) == 22


def test_calculate_score_negative_numbers_raises_exception():
    with pytest.raises(ValueError):
        calculate_score([4, -5, -1, 2])


def test_calculate_score_non_int_raises_exception():
    with pytest.raises(ValueError):
        calculate_score([4, 5, 6, 'a'])


def test_calculate_score_str_raises_exception():
    with pytest.raises(ValueError):
        calculate_score([4, -5, 6, 2])


def test_winner_3_players():
    players = [
      Player(name='player 1', scores=[1, 3, 2, 5]),
      Player(name='player 2', scores=[1, 1, 1, 1]),
      Player(name='player 3', scores=[4, 5, 1, 2]),  # max 9
    ]
    assert get_winner(players) == players[-1]


def test_winner_shorter_score_len_raises_exception():
    players = [
      Player(name='player 1', scores=[4, 3, 5, 5]),
      Player(name='player 2', scores=[4, 4, 6]),  # lacks one score
      Player(name='player 3', scores=[4, 5, 6, 6]),
    ]
    with pytest.raises(ValueError):
        get_winner(players)


def test_winner_longer_score_len_raises_exception():
    players = [
      Player(name='player 1', scores=[4, 3, 5, 5, 4]),
      Player(name='player 2', scores=[4, 4, 6, 6, 3, 2]),  # 1 more
      Player(name='player 3', scores=[4, 5, 6, 6, 5]),
    ]
    with pytest.raises(ValueError):
        get_winner(players)