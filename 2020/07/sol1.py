#!/usr/bin/env python3
import re
from collections import defaultdict


def load_data(filename):
    contained_by = defaultdict(set)
    with open(filename) as fin:
        for line in fin:
            outer, *inner = re.split(
                " \d ", re.sub("( bags?| contain|,|\.|\n)", "", line)
            )
            for bag in inner:
                contained_by[bag].add(outer)
    return contained_by


def find_number_of_valid_bags(contained_by, color):
    valid_bags = set()
    queue = [color]
    while True:
        if not queue:
            break
        size = len(queue)
        for _ in range(size):
            cur = queue.pop(0)
            for bag in contained_by[cur]:
                if bag in valid_bags:
                    continue
                valid_bags.add(bag)
                queue.append(bag)
    return len(valid_bags)


if __name__ == "__main__":
    contained_by = load_data("input")
    print(find_number_of_valid_bags(contained_by, "shiny gold"))
