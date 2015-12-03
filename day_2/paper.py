import os


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


def total_paper(box):
    side1 = box.length*box.width
    side2 = box.width*box.height
    side3 = box.height*box.length
    surface = (side1 + side2 + side3)*2
    slack = min(side1, side2, side3)
    total = surface + slack
    return total


def parse_line(str_line):
    params = str_line.split('x')
    dimensions = list(map(int, params))
    return dimensions


def total_ribbon(box):
    side1 = (box.length+box.width)*2
    side2 = (box.width+box.height)*2
    side3 = (box.height+box.length)*2
    ribbon_len = min(side1, side2, side3)
    bow_len = box.length*box.width*box.height
    total = ribbon_len + bow_len
    return total


if __name__ == '__main__':
    paper = 0
    ribbon = 0
    with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as f:
        content = f.readlines()

    for line in content:
        dim = parse_line(line)
        box = Box(dim[0], dim[1], dim[2])
        paper += total_paper(box)
        ribbon += total_ribbon(box)

    print("Total area: {}".format(paper))
    print("Total ribbon: {}".format(ribbon))















