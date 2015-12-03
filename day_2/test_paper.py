import pytest
from day_2.paper import *


@pytest.mark.parametrize("box, expected", [
    (Box(2, 3, 4), 58),
    (Box(1, 1, 10), 43)
])
def test_total_paper(box, expected):
    assert total_paper(box) == expected


@pytest.mark.parametrize("str, l, w, h", [
    ("23x15x10", 23, 15, 10)
])
def test_parse_line(str, l, w, h):
    dim = parse_line(str)
    assert (dim[0], dim[1], dim[2]) == (l, w, h)


@pytest.mark.parametrize("box, expected", [
    (Box(2, 3, 4), 34),
    (Box(1, 1, 10), 14)
])
def test_total_ribbon(box, expected):
    assert total_ribbon(box) == expected
