from distutils.version import LooseVersion as lv

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old_reqs_split = dict(item.split('==') for item in old_reqs.split())
    new_reqs_split = dict(item.split('==') for item in new_reqs.split())
    
    # result = list({key for key in old_result = list({key for key in old_reqs_split if key in new_reqs_split and old_reqs_split[key] < new_reqs_split[key]})
    # return result
    
    result = list()
    for key in old_reqs_split:
        old_version = old_reqs_split[key]
        new_version = new_reqs_split[key]
        if lv(old_version) < lv(new_version):
            result.append(key)
    return sorted(result)


# tests
from reqs import changed_dependencies

# version might be fictitious for testing purposes
old_reqs = """
certifi==2017.4.17
chardet==3.0.4
click==6.7
Faker==0.7.12
Flask==0.12.1
"""
new_reqs = """
certifi==2016.11.29
chardet==2.0.4
click==5.0
Faker==1.0.2
Flask==1.0.2
"""
other_old_reqs = """
twilio==6.23.1
urllib3==1.21.1
Werkzeug==0.12.1
WTForms==1.19.0
"""
other_new_reqs = """
twilio==6.3.0
urllib3==1.21.1
Werkzeug==0.14.1
WTForms==2.1
"""


def test_changed_dependencies_old_vs_new():
    actual = changed_dependencies(old_reqs, new_reqs)
    expected = ['Faker', 'Flask']
    assert sorted(actual) == expected


def test_changed_dependencies_other_data():
    actual = changed_dependencies(other_old_reqs, other_new_reqs)
    expected = ['WTForms', 'Werkzeug']
    assert sorted(actual) == expected