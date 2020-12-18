#!/usr/bin/env python3


precedence = {"+": 2, "*": 1, "(": 0}


def infix_to_suffix(expression):
    output = ""
    ops = []
    for c in expression:
        if c == " ":
            continue
        elif "0" <= c <= "9":
            output += c
        elif c in "*+":
            if not ops or precedence[c] > precedence[ops[-1]]:
                ops.append(c)
            else:
                while ops and precedence[c] <= precedence[ops[-1]]:
                    output += ops.pop()
                ops.append(c)
        elif c == "(":
            ops.append(c)
        else:
            while ops and ops[-1] != "(":
                output += ops.pop()
            if ops and ops[-1] == "(":
                ops.pop()
    while ops:
        output += ops.pop()
    return output


def evaluate(expression):
    exp = infix_to_suffix(expression)
    values = []
    for c in exp:
        if "0" <= c <= "9":
            values.append(int(c))
        else:
            first, second = values.pop(), values.pop()
            values.append(first + second if c == "+" else first * second)
    return values[-1]


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(sum(map(evaluate, data)))
