#!/usr/bin/env python3


def is_valid(passport):
    keys = set(field.split(":")[0] for field in passport.replace("\n", " ").split())
    return len(keys) == 8 or (len(keys) == 7 and "cid" not in keys)


if __name__ == "__main__":
    data = open("input").read().split("\n\n")
    print(sum(is_valid(passport) for passport in data))
