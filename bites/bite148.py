from itertools import groupby

cars = [
    # need mock data? -> https://www.mockaroo.com == awesome
    ('Mercedes-Benz', '300D'), ('Mercedes-Benz', '600SEL'),
    ('Toyota', 'Avalon'), ('Ford', 'Bronco'),
    ('Chevrolet', 'Cavalier'), ('Chevrolet', 'Corvette'),
    ('Mercedes-Benz', 'E-Class'), ('Hyundai', 'Elantra'),
    ('Volkswagen', 'GTI'), ('Toyota', 'Highlander'),
    ('Chevrolet', 'Impala'), ('Nissan', 'Maxima'),
    ('Ford', 'Mustang'), ('Kia', 'Optima'),
    ('Volkswagen', 'Passat'), ('Nissan', 'Pathfinder'),
    ('Volkswagen', 'Routan'), ('Hyundai', 'Sonata'),
    ('Kia', 'Sorento'), ('Kia', 'Sportage'),
    ('Ford', 'Taurus'), ('Nissan', 'Titan'),
    ('Toyota', 'Tundra'), ('Hyundai', 'Veracruz'),
]


def group_cars_by_manufacturer(cars):
    """Iterate though the list of (manufacturer, model) tuples
       of the cars list defined above and generate the output as described
       in the Bite description (see the tests for the full output).
       
       No return here, just print to the console. We use pytest > capfd to
       validate your output :)
    """
    group_sort_cars = groupby(sorted(cars), key=lambda car: car[0])
    
    for manufacturer, group in group_sort_cars:
        print(f"{manufacturer.upper()}")
        for g in group:
            print(f"- {g[1]}")
        print()



# tests
from grouping import cars, group_cars_by_manufacturer

expected_output = """
CHEVROLET
- Cavalier
- Corvette
- Impala

FORD
- Bronco
- Mustang
- Taurus

HYUNDAI
- Elantra
- Sonata
- Veracruz

KIA
- Optima
- Sorento
- Sportage

MERCEDES-BENZ
- 300D
- 600SEL
- E-Class

NISSAN
- Maxima
- Pathfinder
- Titan

TOYOTA
- Avalon
- Highlander
- Tundra

VOLKSWAGEN
- GTI
- Passat
- Routan
"""


def test_group_cars_by_manufacturer(capfd):
    group_cars_by_manufacturer(cars)
    actual_output, _ = capfd.readouterr()
    assert actual_output.strip() == expected_output.strip()