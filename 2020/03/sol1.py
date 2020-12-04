#!/usr/bin/env python3


def number_of_trees(data):
    nrows, ncolumns = len(data), len(data[0])
    row = column = ntrees = 0
    while row < nrows - 1:
        row += 1
        column = (column + 3) % ncolumns
        ntrees += int(data[row][column] == "#")
    return ntrees


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(number_of_trees(data))
