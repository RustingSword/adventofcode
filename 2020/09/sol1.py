#!/usr/bin/env python3


def find_invalid_number(data, preamble=25):
    for idx, target in enumerate(data[preamble:], start=preamble):
        candidates = set(data[idx - preamble : idx])
        if not any(
            (other := target - number) != number and other in candidates
            for number in candidates
        ):
            return target


if __name__ == "__main__":
    data = list(map(int, open("input")))
    print(find_invalid_number(data))
