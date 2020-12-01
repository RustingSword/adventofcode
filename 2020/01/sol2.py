#!/usr/bin/env python3

def find_triple(nums, target=2020):
    for first in nums:
        for second in nums:
            if (third := target - first - second) in nums:
                return first * second * third

if __name__ == "__main__":
    nums = set(map(int, open("input")))
    print(find_triple(nums))
