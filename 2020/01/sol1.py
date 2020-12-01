#!/usr/bin/env python3

data = sorted(map(int, open("input").read().splitlines()))

left = 0
right = len(data) - 1

s = data[left] + data[right]

while s != 2020:
    if s > 2020:
        right -= 1
    else:
        left += 1
    s = data[left] + data[right]

print(data[left] * data[right])
print(f"first={data[left]} second={data[right]}")
