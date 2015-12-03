import os

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

SANTA = 1
ROBOT = -1


def one_present(instructions):
    position = {'x': 0, 'y': 0}
    visited = [{'x': 0, 'y': 0}]
    for c in instructions:
        position = move(position, c)
        if position not in visited:
            visited.append(position)
    return len(visited)


def santa_and_robot(instructions):
    santa = {'x': 0, 'y': 0}
    robot = {'x': 0, 'y': 0}
    visited = [{'x': 0, 'y': 0}]
    turn = SANTA
    for c in instructions:
        if turn == SANTA:
            santa = move(santa, c)
            if santa not in visited:
                visited.append(santa)
        elif turn == ROBOT:
            robot = move(robot, c)
            if robot not in visited:
                visited.append(robot)
        turn *= -1
    return len(visited)


def move(entity, direction):
    new = entity.copy()
    if direction == UP:
        new['y'] += 1
    elif direction == DOWN:
        new['y'] -= 1
    elif direction == LEFT:
        new['x'] -= 1
    elif direction == RIGHT:
        new['x'] += 1
    return new


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as f:
        data = f.read()

    houses = one_present(data)
    houses_with_robot = santa_and_robot(data)
    print("Houses visited at least once: {}".format(houses))
    print("... and with a robot: {}".format(houses_with_robot))











