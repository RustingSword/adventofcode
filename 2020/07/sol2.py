#!/usr/bin/env python3
import re
from collections import defaultdict


def load_data(filename):
    contains = defaultdict(set)
    with open(filename) as fin:
        for line in fin:
            outer, *inner = re.split(
                " \d ", re.sub("( bags?| contain|,|\.|\n)", "", line)
            )
            numbers = re.findall("\d", line)
            for num, bag in zip(numbers, inner):
                contains[outer].add((int(num), bag))
    return contains


def find_number_of_contained_bags(contains, color):
    queue = [(1, color)]
    num_contained_bags = -1  # outer-most bag not counted
    while True:
        if not queue:
            break
        size = len(queue)
        for _ in range(size):
            num_outer, color_outer = queue.pop(0)
            num_contained_bags += num_outer
            if color_outer not in contains:
                continue
            for num_inner, color_inner in contains[color_outer]:
                next_bag = (num_outer * num_inner, color_inner)
                queue.append(next_bag)
    return num_contained_bags


if __name__ == "__main__":
    contains = load_data("input")
    print(find_number_of_contained_bags(contains, "shiny gold"))
