#!/usr/bin/env python3

import sys


def get_arg() -> int:
    if len(sys.argv) != 2:
        print('Usage: ex1.py <input_file>')
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += int(line)

    return total


def calc(nb: int) -> int:
    temp_nb: int = nb
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
