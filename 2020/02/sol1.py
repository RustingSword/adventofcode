#!/usr/bin/env python3


def valid_password_num(data):
    def is_valid(line):
        rule, char, password = line.replace(":", "").split()
        min_cnt, max_cnt = map(int, rule.split("-"))
        return min_cnt <= password.count(char) <= max_cnt

    print(sum(is_valid(line) for line in data))


if __name__ == "__main__":
    data = open("input").read().splitlines()
    valid_password_num(data)
