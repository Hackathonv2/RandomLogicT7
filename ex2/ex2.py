#!/usr/bin/env python3

import sys


def get_arg() -> list[str]:
    if len(sys.argv) != 2:
        print('Usage: ex1.py <input_file>')
        sys.exit(1)

    file1 = open(sys.argv[1])
    lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in lines:
        count += 1

    return lines


def check_storm(argument: list[str]) -> None:
    first_line: str = argument[0]
    first_line = first_line.strip()
    second_line: str = argument[1]
    second_line = second_line.strip()
    strkeep: str = ''
    strkeep2: str = ''

    for x in range(len(first_line)):
        for y in range(len(second_line)):
            if first_line[x] == second_line[y]:
                strkeep += first_line[x]

    for x in range(len(second_line)):
        for y in range(len(first_line)):
            if second_line[x] == first_line[y]:
                strkeep2 += second_line[x]

    if strkeep == strkeep2:
        print('TEMPETE')
        print(strkeep)
    else:
        print('NORMAL')


if __name__ == '__main__':
    argument: list[str] = get_arg()
    check_storm(argument)
