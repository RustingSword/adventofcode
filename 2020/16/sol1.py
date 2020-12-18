#!/usr/bin/env python3


def scan(rules, tickets):
    def span(spec):
        start, end = spec.split("-")
        return set(range(int(start), int(end) + 1))

    all_valid_numbers = set()
    for rule in rules:
        name, valid = rule.split(": ")
        first, second = valid.split(" or ")
        all_valid_numbers |= span(first) | span(second)

    res = []
    for idx, ticket in enumerate(tickets, start=1):
        numbers = list(map(int, ticket.split(",")))
        for number in numbers:
            if number not in all_valid_numbers:
                res.append(number)
    return sum(res)


if __name__ == "__main__":
    rules, mine, tickets = open("input").read().split("\n\n")
    print(scan(rules.splitlines(), tickets.splitlines()[1:]))
