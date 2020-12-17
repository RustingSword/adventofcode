#!/usr/bin/env python3


def speak(data, target=2020):
    pos = {num: (idx, 0) for idx, num in enumerate(data, start=1)}
    cur, last = len(data) + 1, data[-1]

    while cur <= target:
        if last in pos:
            first, second = pos[last]
            last = 0 if second == 0 else first - second
        else:
            last = 0
        pos[last] = (cur, pos[last][0] if last in pos else 0)
        cur += 1
    return last


if __name__ == "__main__":
    data = list(map(int, open("input").readline().split(",")))
    print(speak(data))
