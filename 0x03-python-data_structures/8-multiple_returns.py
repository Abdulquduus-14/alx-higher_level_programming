#!/usr/bin/python3

def multiple_returns(sentence):
    """  function that find a tuple's length of a string parameter.
    Args:
    sentence: string to work on
    Return:
    length of string and first letter
    """

    if len(sentence) == 0:
        return (0, 'None')
    else:
        return (len(sentence), sentence[0])
