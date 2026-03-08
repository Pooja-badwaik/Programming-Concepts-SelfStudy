
# 3. Given 2 tuples, perform cross pairing of corresponding tuples, convert to single tuple
# if 1st element of both tuple matches.

# PGCP-ITISS

# Sunbeam Institute of Information Technology

# Input : test_list1 = [(1, 7), (6, 7), (8, 100), (4, 21)],
# test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]
# Output : [(7, 3)]
# Explanation : 1 occurs as tuple element at pos. 1 in both tuple, its 2nd
# elements are paired and returned.
# Input : test_list1 = [(10, 7), (6, 7), (8, 100), (4, 21)],
# test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]
# Output : [ ]
# Explanation : NO pairing possible.






test_list1 = [(1, 7), (6, 7), (8, 100), (4, 21)]
test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

result = []

for a in test_list1:
    for b in test_list2:
        if a[0] == b[0]:     # check first element
            result.append((a[1], b[1]))   # pair second elements

print(result)