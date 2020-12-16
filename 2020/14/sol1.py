#!/usr/bin/env python3


def write(mem, addr, value, mask):
    value = bin(value)[2:].zfill(36)
    masked = "".join(
        ["1" if m == "1" else "0" if m == "0" else x for x, m in zip(value, mask)]
    )
    mem[addr] = int(masked, base=2)


def exec(data):
    mem = {}
    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            addr, value = line.split(" = ")
            addr = int(addr.split("[")[1].replace("]", ""))
            value = int(value)
            write(mem, addr, value, mask)
    return sum(mem.values())


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(exec(data))
