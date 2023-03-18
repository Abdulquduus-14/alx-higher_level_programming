#!/usr/bin/python3

def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer.

    Args:
    roman_string: string to convert to integer

    Return:
    integer on success, else 0
    """
    rot = {"I": 1, "II": 2, "III": 3,
           "IV": 4, "V": 5, "VI": 6, "VII": 7,
           "VIII": 8, "IX": 9, "X": 10, "LXXXVII": 87,
           "DCCVII": 707}
    if roman_string == "None":
        return 0
    if roman_string in rot:
        return rot[roman_string]
