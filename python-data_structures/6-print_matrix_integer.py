#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                # Add a space before the next number
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()  # Move to the next line for the next row

if _name_ == "_main_":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
