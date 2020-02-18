import pandas as pd
import collections

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    # read data
    pd_data = pd.read_csv(data, index_col=0)
    
    # ==> one way
    # male_most_medals = dict(pd_data[pd_data["Gender"] == "Men"]["Athlete"].value_counts().head(1))
    # female_most_medals = dict(pd_data["Athlete"][pd_data["Gender"] == "Women"].value_counts().head(1))
    
    # merge dicts
    # return {**male_most_medals, **female_most_medals}
    
    # ==> another way
    f_medals = dict(collections.Counter(pd_data["Athlete"][pd_data["Gender"] == 'Women']).most_common(1))
    m_medals = dict(collections.Counter(pd_data["Athlete"][pd_data["Gender"] == 'Men']).most_common(1))
    most_medals = {**f_medals, **m_medals}
    return most_medals


# tests
from medals import data, athletes_most_medals


def test_athletes_most_medals_default_csv():
    ret = athletes_most_medals()
    assert len(ret) == 2
    assert ret["LATYNINA, Larisa"] == 18
    assert ret["PHELPS, Michael"] == 22


def test_smaller_csv_and_guarantee_checking_male_and_female():
    ret = athletes_most_medals(
        data.replace('summer', 'summer_2008-2012')
    )
    assert len(ret) == 2
    assert ret["PHELPS, Michael"] == 14
    assert ret["COUGHLIN, Natalie"] == 7  # not LOCHTE, Ryan