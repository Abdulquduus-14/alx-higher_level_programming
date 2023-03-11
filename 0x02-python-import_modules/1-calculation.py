#!/usr/bin/python3

from calculator_1 import add, sub, mul, div


def main():
    """My main function

    Args:
        a: first integer
        b: second integer

    Returns:
        0 for success
    """


a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
print(a, "+", b, "=", sub(a, b))
main()
