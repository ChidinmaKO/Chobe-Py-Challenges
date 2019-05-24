from functools import reduce
def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    #   using reduce
    # result = reduce(set.intersection, map(set, programmers.values()))
    # return result
    
    # using plain ol' map
    result2 = set.intersection(*map(set, programmers.values()))
    return result2