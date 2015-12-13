import hashlib

my_input = 'ckczppom'


def mine(secret_key, beg='00000'):
    lowest = 1

    while True:
        md5 = hashlib.md5()
        mystr = '{}{}'.format(secret_key, str(lowest)).encode(encoding='UTF-8')
        md5.update(mystr)
        if md5.hexdigest().startswith(beg):
            return lowest
        else:
            lowest += 1


if __name__ == '__main__':
    print(mine(my_input))
    print(mine(my_input, beg='000000'))
