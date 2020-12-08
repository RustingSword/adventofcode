#!/usr/bin/env python3


def run(instructions):
    executed, addr, accumulator = set(), 0, 0
    while True:
        if addr in executed:
            return accumulator
        executed.add(addr)
        instr, arg = instructions[addr]
        accumulator += arg if instr == "acc" else 0
        addr += arg if instr == "jmp" else 1


if __name__ == "__main__":
    instructions = [(line.split()[0], int(line.split()[1])) for line in open("input")]
    print(run(instructions))
