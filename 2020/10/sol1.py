#!/usr/bin/env python3


def connect(data):
    diff = {1: 1, 3: 1}
    data.sort()
    for prev, next in zip(data[:-1], data[1:]):
        diff[next - prev] += 1
    return diff[1] * diff[3]


if __name__ == "__main__":
    data = list(map(int, open("input")))
    print(connect(data))
