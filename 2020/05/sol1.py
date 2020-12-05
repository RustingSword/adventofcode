#!/usr/bin/env python3


def bisearch(string):
    low, high = 0, 2 ** len(string) - 1
    for direction in string:
        mid = (low + high) // 2
        if direction in ("F", "L"):
            high = mid
        else:
            low = mid + 1
    return (low + high) // 2


def calc_seat_id(line):
    row = bisearch(line[:7])
    col = bisearch(line[7:])
    return row * 8 + col


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(max(calc_seat_id(seat) for seat in data))
