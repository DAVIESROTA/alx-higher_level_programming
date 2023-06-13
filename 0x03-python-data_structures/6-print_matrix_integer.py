#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for s in matrix:
        print(" ".join("{:d}".format(p) for p in s))
