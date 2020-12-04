#!/usr/bin/env python3

rules = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or \
                     (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: x[0] == "#" and all(c in "0123456789abcdef" for c in x[1:]),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: len(x) == 9 and 0 < int(x) < 999999999,
    "cid": lambda x: True,
}


def is_valid(passport):
    kv = dict(field.split(":") for field in passport.replace("\n", " ").split())
    return all(rules[k](kv.get(k, "-1")) for k in rules)


if __name__ == "__main__":
    data = open("input").read().split("\n\n")
    print(sum(is_valid(passport) for passport in data))
