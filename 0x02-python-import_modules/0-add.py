#!/usr/bin/python3

from add_0 import add


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

main()
