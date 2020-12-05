#!/usr/bin/env python3


def find_pair(nums, target=2020):
    for first in nums:
        if (second := target - first) in nums:
            return first * second


if __name__ == "__main__":
    nums = set(map(int, open("input")))
    print(find_pair(nums))
