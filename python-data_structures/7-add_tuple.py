#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use 0 for each missing integer
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)

    # Add the first elements and the second elements of the two tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result

if _name_ == "_main_":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
