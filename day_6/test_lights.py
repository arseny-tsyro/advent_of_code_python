import pytest
from day_6.lights import *


@pytest.mark.parametrize("instr, expected", [
    ("turn on 0,0 through 2,2", [[ON for col in range(3)] for row in range(3)]),
    ("toggle 0,0 through 2,0", [[ON, ON, ON],
                                [OFF, OFF, OFF],
                                [OFF, OFF, OFF]]),
    ("turn off 1,1 through 2,2", [[OFF for col in range(3)] for row in range(3)])
])
def test_read_instruction(instr, expected):
    grid = [[OFF for col in range(3)] for row in range(3)]
    read_instruction(instr, grid)
    assert grid == expected

