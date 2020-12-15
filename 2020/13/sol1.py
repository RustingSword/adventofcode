#!/usr/bin/env python3


def earliest_bus(ts, bus_ids):
    wait = [(bus_id - ts % bus_id) % bus_id for bus_id in bus_ids]
    minute = min(wait)
    bus_id = wait.index(minute)
    return minute * bus_ids[bus_id]


if __name__ == "__main__":
    ts, bus_ids = open("input").read().splitlines()
    bus_ids = [int(x) for x in bus_ids.split(",") if x != "x"]
    print(earliest_bus(int(ts), bus_ids))
