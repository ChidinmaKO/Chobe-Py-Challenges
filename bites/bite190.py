# Bite 190. Parse income distribution from Latin America XML

from pathlib import Path
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET
from collections import defaultdict

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    with open(countries, 'r') as xmlf:
        tree = ET.parse(xmlf)
        root = tree.getroot()
        
        income_dist = defaultdict(list)
        
        for country in root.iter("{http://www.worldbank.org}country"):
            incomeLevel = country.find("{http://www.worldbank.org}incomeLevel").text
            name = country.find("{http://www.worldbank.org}name").text
            income_dist[incomeLevel].append(name)
        return income_dist

# tests
import pytest

# from income import get_income_distribution

EXPECTED = {'High income': ['Aruba',
                            'Argentina',
                            'Antigua and Barbuda',
                            'Bahamas, The',
                            'Barbados',
                            'Chile',
                            'Curacao',
                            'Cayman Islands',
                            'St. Kitts and Nevis',
                            'St. Martin (French part)',
                            'Panama',
                            'Puerto Rico',
                            'Sint Maarten (Dutch part)',
                            'Turks and Caicos Islands',
                            'Trinidad and Tobago',
                            'Uruguay',
                            'British Virgin Islands',
                            'Virgin Islands (U.S.)'],
            'Low income': ['Haiti'],
            'Lower middle income': ['Bolivia',
                                    'Honduras',
                                    'Nicaragua',
                                    'El Salvador'],
            'Upper middle income': ['Belize',
                                    'Brazil',
                                    'Colombia',
                                    'Costa Rica',
                                    'Cuba',
                                    'Dominica',
                                    'Dominican Republic',
                                    'Ecuador',
                                    'Grenada',
                                    'Guatemala',
                                    'Guyana',
                                    'Jamaica',
                                    'St. Lucia',
                                    'Mexico',
                                    'Peru',
                                    'Paraguay',
                                    'Suriname',
                                    'St. Vincent and the Grenadines',
                                    'Venezuela, RB']}


@pytest.fixture(scope="module")
def actual():
    return get_income_distribution()


@pytest.mark.parametrize("income, countries", EXPECTED.items())
def test_return_function(actual, income, countries):
    assert income in actual
    assert sorted(actual[income]) == sorted(countries)