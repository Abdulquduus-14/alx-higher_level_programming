#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists.

    Args:
    my_list_1: first list of elements
    my_list_2: second list of elements
    list_length: length of list

    Returns: a new list
    """
    ls = []
    for i in range(list_length):
        try:
            my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            my_list_1[i] = 0
            my_list_2[i] = 0
        except TypeError:
            print("wrong type")
            my_list_1[i] = 0
            my_list_2[i] = 0
        except IndexError:
            print("out of range")
            my_list_1[i] = 0
            my_list_2[i] = 0
        finally:
            ls[i] = my_list_1[i] / my_list_2[i]
    return (ls)
