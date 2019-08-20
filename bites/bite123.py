from collections import defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships=friendships):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    friend_list = defaultdict(list)
    for i, j in friendships:
        friend1 = users[i]
        friend2 = users[j]
        friend_list[friend1].append(friend2)
        friend_list[friend2].append(friend1)
    user_name = sorted(friend_list, key=lambda friend: len(friend_list[friend]), reverse=True)[0]
    user_friends = friend_list[user_name]
    return user_name, user_friends
    
# tests
# from friends import get_friend_with_most_friends


def test_get_friend_with_most_friends_default_arg():
    user, friends = get_friend_with_most_friends()
    assert user == 'sara'
    assert sorted(list(friends)) == ['joyce', 'kevin', 'nick', 'rod']


def test_get_friend_with_most_friends_different_friendship_data():
    friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]
    user, friends = get_friend_with_most_friends(friendships)
    assert user == 'joyce'
    assert sorted(list(friends)) == ['beverly', 'julian', 'kevin', 'nick',
                                     'rod', 'sara']