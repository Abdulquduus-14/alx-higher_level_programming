#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    """My main function

    Args:
        a: first integer
        b: second integer

    Returns:
        0 for success
    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
