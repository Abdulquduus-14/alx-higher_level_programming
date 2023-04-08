#!/usr/bin/python3
""" a function that prints a text with 2 new lines after each
 of these characters: ., ? and : """


def text_indentation(text):
    """ a function that prints a text with 2 new lines
     after each of these characters: ., ? and :

     Args:
     text: string to print

     Returns: Nothing
     """
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")
    for ch in text:
        print(ch, end='')
        if ch == ':' or ch == '?' or ch == '.':
            print("\n")
