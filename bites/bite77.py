def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    my_cities = set(my_cities)
    other_cities = set(other_cities)
    my_cities.symmetric_difference_update(other_cities)
    return len(my_cities)

    # shorter way
    # return len(set(my_cities) ^ set(other_cities))