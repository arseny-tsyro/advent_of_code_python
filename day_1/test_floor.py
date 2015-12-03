import pytest
from day_1.floor import *


@pytest.mark.parametrize("in1, in2, expected", [
    ('(())', '()()', 0),
    ('(((', '(()(()(', 3),
    ('))(((((', '(((', 3),
    ('())', '))(', -1),
    (')))', ')())())', -3)
])
def test_final_floor(in1, in2, expected):
    assert final_floor(in1) == expected
    assert final_floor(in2) == expected
    assert final_floor(in1) == final_floor(in2)


@pytest.mark.parametrize("s, expected", [
    (')', 1),
    ('()())', 5)
])
def test_first_basement(s, expected):
    assert first_basement(s) == expected
