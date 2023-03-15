#!/usr/bin/python3

if __name__ = "__main__":
    """ prints the number of and the list of its arguments.
    """

    print("{:d}".format(len(argv), end=" ")
            if len(argv) == 1:
            print("{:s}".format("argument"))
            else:
            print("{:s}".format("arguments"))
    print("{:s}".format("." if len(argv) == 0 else ":"))

    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
