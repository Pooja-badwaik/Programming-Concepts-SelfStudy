# 1. Write a Python function swap_tuple_elements(tup, i, j) that takes a tuple tup and
# two indices i and j as input. The function should return a new tuple where the
# elements at indices i and j are swapped.
# input_tuple = (10, 20, 30, 40)
# swap_tuple_elements(input_tuple, 1, 3)
# # Expected output: (10, 40, 30, 20)


def swap_tuple_elements(tup, i, j):
    l = list(tup)
    l[i], l[j] = l[j], l[i]
    return tuple(l)

t = (10, 20, 30, 40)
print(swap_tuple_elements(t, 1, 3))