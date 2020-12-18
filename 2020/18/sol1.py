#!/usr/bin/env python3


def evaluate(expression):
    operators, operands = [], []
    expression = expression.replace(" ", "")

    def calc():
        if operators and operators[-1] != "(" and len(operands) >= 2:
            op = operators.pop()
            first, second = operands.pop(), operands.pop()
            operands.append(first + second if op == "+" else first * second)
            return True
        return False

    i = 0
    while i < len(expression):
        c = expression[i]
        if c in "+*":
            calc()
            operators.append(c)
        elif c == "(":
            operators.append(c)
        elif c == ")":
            while calc():
                pass
            operators.pop()
        else:
            operands.append(int(c))
        i += 1
    while calc():
        pass
    return operands[-1]


if __name__ == "__main__":
    data = open("input").read().splitlines()
    print(sum(map(evaluate, data)))
