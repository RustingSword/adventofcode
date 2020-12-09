#!/usr/bin/env python3


def find_invalid_number(data, preamble=25):
    for idx, target in enumerate(data[preamble:], start=preamble):
        candidates = set(data[idx - preamble : idx])
        if not any(
            (other := target - number) != number and other in candidates
            for number in candidates
        ):
            return idx, target


def find_contiguous_set(data, idx, target):
    for i in range(idx - 1):
        for j in range(i + 1, idx):
            if sum(data[i : j + 1]) == target:
                return min(data[i : j + 1]) + max(data[i : j + 1])


if __name__ == "__main__":
    data = list(map(int, open("input")))
    idx, target = find_invalid_number(data)
    print(find_contiguous_set(data, idx, target))
