import pytest
from day_5.nice_strings import *


@pytest.mark.parametrize("string, expected", [
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', False),
    ('haegwjzuvuyypxyu', False),
    ('dvszwmarrgswjxmb', False)
])
def test_is_nice(string, expected):
    result = is_nice(string)
    assert result == expected


@pytest.mark.parametrize("string, expected", [
    ('qjhvhtzxzqqjkmpb', True),
    ('xxyxx', True),
    ('uurcxstgmygtbstg', False),
    ('ieodomkazucvgmuy', False)
])
def test_is_nice_v2(string, expected):
    result = is_nice_v2(string)
    assert result == expected
