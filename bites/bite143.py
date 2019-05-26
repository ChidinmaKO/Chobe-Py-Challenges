from collections import ChainMap
NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if not (type(name) == str):
        return NOT_FOUND
    
    # Method 1
    for k, v in {**group1, **group2, **group3}.items():
        if k == name.lower():
            return v
    return NOT_FOUND

    # Method 2
    # Another way is to use ChainMap from the collections module.
    # ChainMap is used to combine several dictionaries and it returns a list of dictionaries.
    chain_map = ChainMap(group3, group2, group1)
    result = chain_map.get(name, NOT_FOUND)
    return result
    