#!/usr/bin/env python3
from numpy import prod


def number_of_trees(data, row_step, column_step):
    nrows, ncolumns = len(data), len(data[0])
    row = column = ntrees = 0
    while row < nrows - row_step:
        row += row_step
        column = (column + column_step) % ncolumns
        ntrees += int(data[row][column] == "#")
    return ntrees


if __name__ == "__main__":
    data = open("input").read().splitlines()
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print(
        prod(
            [
                number_of_trees(data, row_step, column_step)
                for row_step, column_step in slopes
            ]
        )
    )
