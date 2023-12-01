#!/usr/bin/env python3

import sys


def get_arg() -> int:
    total = eval(sys.stdin.read())
    return total


def calc(number: int) -> int:
    temp_nb: int = number
    for i in range(0, 4):
        if temp_nb % 3 == 0:
            temp_nb = int(temp_nb / 3)
        elif temp_nb % 2 == 0:
            temp_nb = int(temp_nb / 2)
        else:
            temp_nb = temp_nb - 1
    return temp_nb


if __name__ == '__main__':
    nb: int = get_arg()
    final_nb: int = calc(nb)
    print(final_nb)
