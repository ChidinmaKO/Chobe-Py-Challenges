def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if type(data) == dict:
        # return list([*zip(*data.items())])
        return list(map(tuple, zip(*data.items())))
    elif type(data) == list:
        return list(zip(*data))
    else:
        return None
        

# tests
from random import randint
from collections import namedtuple

POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13,
         '2017-11': 12, '2017-12': 11, '2018-1': 3}
NAMES = ['Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard']

Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')


def _gen_community():
    for name in NAMES:
        yield Member(name=name,
                     since_days=randint(1, 365),
                     karma_points=randint(1, 100),
                     bitecoin_earned=randint(1, 100))


def test_transpose_dict():
    months, num_posts = transpose(POSTS)
    assert list(months) == ['2017-8', '2017-9', '2017-10',
                            '2017-11', '2017-12', '2018-1']
    assert list(num_posts) == [19, 13, 13, 12, 11, 3]


def test_transpose_list_tuplies():
    community = list(_gen_community())
    names, days, karma, bitecoin = transpose(community)
    assert list(names) == NAMES
    assert list(days) == [m.since_days for m in community]
    assert list(karma) == [m.karma_points for m in community]
    assert list(bitecoin) == [m.bitecoin_earned for m in community]