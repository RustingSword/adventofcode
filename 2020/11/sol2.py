#!/usr/bin/env python3
import copy
from itertools import product


def num_adjacent_occupied(seats, row, column):
    nrows, ncols, num = len(seats), len(seats[0]), 0
    for i, j in product((1, 0, -1), (1, 0, -1)):
        if i == 0 and j == 0:
            continue
        x, y = row + i, column + j
        while 0 <= x < nrows and 0 <= y < ncols:
            if seats[x][y] == "#":
                num += 1
                break
            if seats[x][y] != ".":  # until it sees first seat
                break
            x += i
            y += j
    return num


def update(seats, row, column):
    if seats[row][column] == "L" and num_adjacent_occupied(seats, row, column) == 0:
        return "#"
    if seats[row][column] == "#" and num_adjacent_occupied(seats, row, column) >= 5:
        return "L"
    return seats[row][column]


def apply_rules(seats):
    nrows, ncols = len(seats), len(seats[0])
    new = copy.deepcopy(seats)
    for i in range(nrows):
        for j in range(ncols):
            new[i][j] = update(seats, i, j)
    return new


def run(seats):
    previous, step = [], 0
    while seats != previous:
        previous, seats = copy.deepcopy(seats), apply_rules(seats)
        step += 1
    print(step)
    num_occupied = sum(1 if seat == "#" else 0 for row in seats for seat in row)
    print("\n".join("".join(s) for s in seats))
    return num_occupied


if __name__ == "__main__":
    seats = list(map(list, open("input").read().splitlines()))
    print(run(seats))
