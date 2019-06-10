def get_index_different_char(chars):
    alnum = []
    not_alnum = []
    
    for index, char in enumerate(chars):
        if str(char).isalnum():
            alnum.append(index)
        else:
            not_alnum.append(index)
    result = alnum[0] if len(alnum) < len(not_alnum) else not_alnum[0]
    return result


# tests
def test_wrong_char():
    inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),  # noqa E231
    )
    expected = [2, 4, 1, 5, 8]

    for arg, exp in zip(inputs, expected):
        err = f'get_index_different_char({arg}) should return index {exp}'
        assert get_index_different_char(arg) == exp, err