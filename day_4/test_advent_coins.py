import pytest
from day_4.advent_coins import *


@pytest.mark.parametrize("secret_key, expected", [
    ("abcdef", 609043),
    ("pqrstuv", 1048970)
])
def test_mine(secret_key, expected):
    result = mine(secret_key)
    assert result == expected
