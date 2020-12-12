#!/usr/bin/env python3


def navigate(instructions):
    waypoint = (10, 1)
    h = v = 0
    for instruction in instructions:
        action, unit = instruction[0], int(instruction[1:])
        x, y = waypoint
        if action in ("L", "R"):
            waypoint = {90: (y, -x), 180: (-x, -y), 270: (-y, x)}[
                {"L": 360 - unit, "R": unit}[action]
            ]
        elif action in "ESWN":
            direction = {"E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0, 1)}[action]
            waypoint = (x + direction[0] * unit, y + direction[1] * unit)
        else:
            h += waypoint[0] * unit
            v += waypoint[1] * unit
    return abs(h) + abs(v)


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(navigate(data))
