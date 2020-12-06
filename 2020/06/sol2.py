#!/usr/bin/env python3
import string


def num_of_uniq_question(group):
    res = set(string.ascii_lowercase)
    for answer in group.split("\n"):
        res &= set(answer)
    return len(res)


if __name__ == "__main__":
    data = open("input").read().split("\n\n")
    print(sum(num_of_uniq_question(group) for group in data))
