import os

UP = '('
DOWN = ')'


def final_floor(str_input):
    floor = 0
    for s in str_input:
        if s == UP:
            floor += 1
        elif s == DOWN:
            floor -= 1
    return floor


def first_basement(str_input):
    floor = 0
    for i, s in enumerate(str_input):
        if s == UP:
            floor += 1
        elif s == DOWN:
            floor -= 1
        if floor == -1:
            return i+1


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')) as f:
        data = f.read()
        floor = final_floor(data)
        basement = first_basement(data)
        print("Final floor: " + str(floor))
        print("Basement index: " + str(basement))
