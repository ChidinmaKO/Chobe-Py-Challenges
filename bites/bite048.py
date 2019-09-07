# Bite 48. Make a bar chart of new Safari books

import os
import urllib.request
import re

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    to_slack = "sending to slack channel"
    key = "python"
    previous_book = ""
    book = ""
    chart = {}
    
    with open(LOG, "r") as f:
        for row in f:
            log = re.split("\s+", row.strip(), 5)
            
            if to_slack not in log[5]:
                previous_book = log[5]

            else:
                if key in previous_book.lower():
                    book = PY_BOOK
                else:
                    book = OTHER_BOOK
                    
                if log[0] in chart:
                    chart[log[0]] += book
                else:
                    chart[log[0]] = book
    for k,v in chart.items():
        print(f"{k} {v}")

# tests
# from safari import create_chart

expected_lines = """02-13 ...........
02-14 ..............
02-15 .................
02-16 ............
02-19 🐍.......🐍
02-20 ...
02-21 ..............🐍
02-22 🐍...................""".split('\n')

def test_valid_output(capfd):
    create_chart()
    out, _ = capfd.readouterr()
    for line in expected_lines:
        assert line in out, f'"{line}" should be in output of create_chart'
    
    