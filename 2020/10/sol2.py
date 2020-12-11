#!/usr/bin/env python3


def count(data):
    data = sorted(data) + [max(data) + 3]
    dp = {jolt: 0 for jolt in data}
    dp[0] = 1
    for jolt in data:
        dp[jolt] = dp.get(jolt - 3, 0) + dp.get(jolt - 2, 0) + dp.get(jolt - 1, 0)
    return dp[data[-1]]


if __name__ == "__main__":
    data = list(map(int, open("input")))
    print(count(data))
