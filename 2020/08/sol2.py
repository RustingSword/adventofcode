#!/usr/bin/env python3
import copy


def run(instructions):
    executed, addr, accumulator = set(), 0, 0
    while True:
        if addr in executed:
            return False, accumulator
        if addr == len(instructions):
            return True, accumulator
        executed.add(addr)
        instr, arg = instructions[addr]
        accumulator += arg if instr == "acc" else 0
        addr += arg if instr == "jmp" else 1


def fix(instructions):
    for addr in range(len(instructions)):
        next_run = copy.deepcopy(instructions)
        instr = next_run[addr]
        if instr[0] not in ("nop", "jmp"):
            continue
        instr[0] = {"nop": "jmp", "jmp": "nop"}[instr[0]]
        fixed, result = run(next_run)
        if fixed:
            return result


if __name__ == "__main__":
    instructions = [[line.split()[0], int(line.split()[1])] for line in open("input")]
    print(fix(instructions))
