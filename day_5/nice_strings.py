import os
import re

vowels = 'aeiou'
bad_substrs = ['ab', 'cd', 'pq', 'xy']


def is_nice(my_string):
    three_vowels = re.search(r"([aeiou].*){3,}", my_string) is not None
    two_in_a_row = re.search(r"(\w)\1", my_string) is not None
    no_bad_strings = re.search(r"ab|cd|pq|xy", my_string) is None
    return three_vowels and two_in_a_row and no_bad_strings


def is_nice_v2(my_string):
    return (re.search(r"(\w\w).*\1", my_string) is not None) and \
           (re.search(r"(\w)\w\1", my_string) is not None)


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as f:
        strings = f.readlines()

    nice_count = 0
    nice_2_count = 0
    for s in strings:
        if is_nice(s):
            nice_count += 1
        if is_nice_v2(s):
            nice_2_count += 1

    print('Nice strings count: {}'.format(nice_count))
    print('Nice strings v2 count: {}'.format(nice_2_count))


