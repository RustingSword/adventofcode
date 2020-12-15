#!/usr/bin/env python3


def earliest_ts(bus_ids):
    bus_delay = [
        (int(bus_id), index) for index, bus_id in enumerate(bus_ids) if bus_id != "x"
    ]
    ts = step = 1
    for bus_id, delay in bus_delay:
        while True:
            if (ts + delay) % bus_id == 0:
                step *= bus_id
                break
            ts += step
    return ts


if __name__ == "__main__":
    _, bus_ids = open("input").read().splitlines()
    bus_ids = bus_ids.split(",")
    print(earliest_ts(bus_ids))
