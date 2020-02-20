import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    # most_calories = df.sort_values(by='Calories', ascending=False).iloc[0].Item
    most_calories = df.loc[df['Calories'].idxmax()].Item
    return most_calories


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    if excl_drinks:
        df = df[(df['Category'] != 'Beverages') & (df['Category'] != 'Coffee & Tea')]
    
    df = df[df['Calories'] != 0]
    df['Protein-Calorie-Ratio'] = df['Protein'] / df['Calories']
    top_five = df.nlargest(n=5, columns='Protein-Calorie-Ratio').Item
    
    return top_five.to_list()

# tests
from mcdonalds import (df,
                       get_food_most_calories,
                       get_bodybuilder_friendly_foods)

ASSERT_ERROR = ("One or more expected foods not in "
                "get_bodybuilder_friendly_foods's return value")


def test_get_food_most_calories():
    actual = get_food_most_calories()
    expected = 'Chicken McNuggets (40 piece)'
    assert actual == expected


def test_get_food_most_calories_smaller_population():
    """Extra test to prevent hardcoding the return value"""
    df_breakfast = df[df['Category'] == 'Breakfast']

    actual = get_food_most_calories(df_breakfast)
    expected = 'Big Breakfast with Hotcakes (Large Biscuit)'
    assert actual == expected


def test_get_bodybuilder_friendly_foods():
    actual_with_drinks = list(get_bodybuilder_friendly_foods())
    expected = ['Premium Bacon Ranch Salad with Grilled Chicken',
                'Nonfat Latte (Small)',
                'Nonfat Latte (Large)',
                'Premium Southwest Salad with Grilled Chicken',
                'Nonfat Latte (Medium)']
    assert all(food in actual_with_drinks for food in expected), ASSERT_ERROR


def test_get_bodybuilder_friendly_foods_excluding_liquid_food():
    actual_wo_drinks = list(get_bodybuilder_friendly_foods(excl_drinks=True))
    expected = ['Premium Bacon Ranch Salad with Grilled Chicken',
                'Premium Southwest Salad with Grilled Chicken',
                'Premium Grilled Chicken Classic Sandwich',
                'Premium Grilled Chicken Ranch BLT Sandwich',
                'Premium Grilled Chicken Club Sandwich']
    assert all(food in actual_wo_drinks for food in expected), ASSERT_ERROR