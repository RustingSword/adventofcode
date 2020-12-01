#!/usr/bin/env python3

data = sorted(map(int, open("input").read().splitlines()))

for idx, num in enumerate(data[:-2]):
    left = idx + 1
    right = len(data) - 1
    target = 2020 - num
    s = data[left] + data[right]
    while s != target and left <= right:
        if s > target:
            right -= 1
        else:
            left += 1
        s = data[left] + data[right]
    if s == target:
        print(num * data[left] * data[right])
        print(f"first={data[idx]} second={data[left]} third={data[right]}")
        break
