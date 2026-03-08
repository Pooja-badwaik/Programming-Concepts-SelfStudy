# Given a list of tuples, where each tuple contains a name (string) and a score (integer),
# write a Python function sort_scores(data) that sorts the list of tuples in descending
# order based on the score.
# scores = [('Alice', 88), ('Bob', 92), ('Charlie', 75), ('David', 92)]
# Expected output: [('Bob', 92), ('David', 92), ('Alice', 88), ('Charlie', 75)]


def sort_scores(data):
    data.sort(key=lambda x: x[1], reverse=True)
    return data

scores = [('Alice', 88), ('Bob', 92), ('Charlie', 75), ('David', 92)]
print(sort_scores(scores))