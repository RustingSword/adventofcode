#!/usr/bin/env python3


def valid_password_num(data):
    def is_valid(line):
        rule, char, password = line.replace(":", "").split()
        first_pos, second_pos = map(lambda x: int(x) - 1, rule.split("-"))
        return (password[first_pos] == char) != (password[second_pos] == char)

    print(sum(is_valid(line) for line in data))


if __name__ == "__main__":
    data = open("input").read().splitlines()
    valid_password_num(data)
