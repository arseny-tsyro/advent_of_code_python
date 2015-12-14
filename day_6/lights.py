import re
import os

GRID_WIDTH = 1000
GRID_HEIGHT = 1000
ON = 1
OFF = -1


def read_instruction(s, grid):
    func = re.findall(r"\A(turn on|turn off|toggle)", s)[0]
    coords = re.findall(r"\d*,\d*", s)
    start = coords[0].split(',')
    end = coords[1].split(',')
    for y in range(int(start[1]), int(end[1])+1):
        for x in range(int(start[0]), int(end[0])+1):
            if func == "turn on":
                grid[y][x] = ON
            elif func == "turn off":
                grid[y][x] = OFF
            elif func == "toggle":
                grid[y][x] *= -1


if __name__ == '__main__':
    grid = [[OFF for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]  # grid filled with turned off lights
    with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as f:
        strings = f.readlines()

    for instr in strings:
        read_instruction(instr, grid)

    lit_count = 0
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == ON:
                lit_count += 1

    print("Lit: " + str(lit_count))
