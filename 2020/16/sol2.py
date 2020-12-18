#!/usr/bin/env python3


def scan(rules, mine, tickets):
    rule_value = {}

    def span(spec):
        start, end = spec.split("-")
        return set(range(int(start), int(end) + 1))

    all_valid_numbers = set()
    for rule in rules:
        name, valid = rule.split(": ")
        first, second = valid.split(" or ")
        rule_value[name] = span(first) | span(second)
        all_valid_numbers |= span(first) | span(second)

    valid_tickets = []
    for idx, ticket in enumerate(tickets, start=1):
        numbers = list(map(int, ticket.split(",")))
        if all(number in all_valid_numbers for number in numbers):
            valid_tickets.append(numbers)

    possible_field = [set(rule_value.keys()) for _ in range(len(rule_value))]

    for numbers in valid_tickets:
        for idx, number in enumerate(numbers):
            for rule_name, valid in rule_value.items():
                if number not in valid:
                    if rule_name in possible_field[idx]:
                        possible_field[idx].remove(rule_name)
    fixed_fields = set()
    correct_fields = sorted(
        [(idx, candidates) for idx, candidates in enumerate(possible_field)],
        key=lambda x: len(x[1]),
    )
    for idx, field in enumerate(correct_fields):
        correct_fields[idx] = (field[0], field[1] - fixed_fields)
        fixed_fields |= field[1]
    correct_fields.sort(key=lambda x: x[0])
    field_names = [field[1].pop() for field in correct_fields]

    res = 1
    for idx, value in enumerate(map(int, mine.split(","))):
        if field_names[idx].startswith("departure"):
            res *= value

    return res


if __name__ == "__main__":
    rules, mine, tickets = open("input").read().split("\n\n")
    print(scan(rules.splitlines(), mine.splitlines()[1], tickets.splitlines()[1:]))
