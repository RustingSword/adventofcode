#!/usr/bin/env python3


def write(mem, addr, value, mask):
    addr = bin(addr)[2:].zfill(36)
    masked = "".join(
        ["X" if m == "X" else "1" if m == "1" else x for x, m in zip(addr, mask)]
    )

    def write_decode(mem, addr, value, index):
        if addr.count("X") == 0:
            mem[int(addr, base=2)] = value
            return
        if addr[index] == "X":
            addr0 = addr[:index] + "0" + addr[index + 1 :]
            write_decode(mem, addr0, value, index + 1)
            addr1 = addr[:index] + "1" + addr[index + 1 :]
            write_decode(mem, addr1, value, index + 1)
        else:
            write_decode(mem, addr, value, index + 1)

    write_decode(mem, masked, value, 0)


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
