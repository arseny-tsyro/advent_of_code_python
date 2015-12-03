import pytest
from day_3.house import *


@pytest.mark.parametrize("instructions, expected", [
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2)
])
def test_one_present(instructions, expected):
    assert one_present(instructions) == expected


@pytest.mark.parametrize("instructions, expected", [
    ('^v', 3),
    ('^>v<', 3),
    ('^v^v^v^v^v', 11)
])
def test_santa_and_robot(instructions, expected):
    assert santa_and_robot(instructions) == expected
