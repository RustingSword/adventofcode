#!/usr/bin/env python3
from itertools import product


def step(cubes):
    state = cubes.items()

    expand = {}
    for cube in state:
        (x, y, z), active = cube
        for dx, dy, dz in product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1)):
            grid = (x + dx, y + dy, z + dz)
            expand[grid] = cubes.get(grid, ".")

    for cube in expand.items():
        (x, y, z), active = cube
        num_active = 0
        for i, (dx, dy, dz) in enumerate(product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1))):
            if dx == dy == dz == 0:
                continue
            grid = (x + dx, y + dy, z + dz)
            num_active += expand.get(grid, ".") == "#"
        if active == "#":
            cubes[(x, y, z)] = "#" if num_active in (2, 3) else "."
        else:
            cubes[(x, y, z)] = "#" if num_active == 3 else "."


def simulate(data):
    cubes = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            cubes[(i, j, 0)] = data[i][j]
    for _ in range(6):
        step(cubes)
    return list(cubes.values()).count("#")


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(simulate(data))
