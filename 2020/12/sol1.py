#!/usr/bin/env python3

accu = {x: 0 for x in range(4)}

directions = {x: y for x, y in zip(list("ESWN"), range(4))}


def navigate(instructions):
    facing = 0
    for instruction in instructions:
        action, unit = instruction[0], int(instruction[1:])
        if action in ("L", "R"):
            facing = (facing + (-unit if action == "L" else unit) // 90) % 4
        else:
            direction = directions.get(action, facing)
            accu[direction] += unit
    return abs(accu[0] - accu[2]) + abs(accu[1] - accu[3])


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(navigate(data))
