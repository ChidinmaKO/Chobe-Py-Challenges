import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0
    cap = cap.lstrip("$")
    caps = float(cap.rstrip("B")) * 1000 if "B" in cap else float(cap.rstrip("M"))
    # caps = float(cap[:-1]) * 1000 if "B" in cap else float(cap[:-1])
    return caps


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    sum_cap_industry = sum(_cap_str_to_mln_float(datum["cap"]) for datum in data if industry == datum["industry"])
    return round(sum_cap_industry, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    sorted_cap = sorted(data, key=lambda data: _cap_str_to_mln_float(data["cap"]), reverse=True)
    return sorted_cap[0]["symbol"]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    chosen_sectors = [datum["sector"] for datum in data if datum["sector"] != "n/a"]
    most_common_ = Counter(chosen_sectors).most_common()
    max_stocks_sector = most_common_[0][0]
    min_stocks_sector = most_common_[-1][0]
    return (max_stocks_sector, min_stocks_sector)
    
    
# tests
from stocks import (_cap_str_to_mln_float,
                    get_stock_symbol_with_highest_cap,
                    get_industry_cap,
                    get_sectors_with_max_and_min_stocks)


def test_cap_str_to_mln_float():
    assert _cap_str_to_mln_float('n/a') == 0
    assert _cap_str_to_mln_float('$100.45M') == 100.45
    assert _cap_str_to_mln_float('$20.9B') == 20900


def test_get_stock_symbol_with_highest_cap():
    assert get_stock_symbol_with_highest_cap() == 'JNJ'


def test_get_industry_cap():
    assert get_industry_cap("Business Services") == 368853.27
    assert get_industry_cap("Real Estate Investment Trusts") == 243295.36


def test_get_sectors_with_max_and_min_stocks():
    assert get_sectors_with_max_and_min_stocks() == ('Finance',
                                                     'Transportation')