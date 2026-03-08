
# 1. Given a string, find the length of the longest substring that does not contain any
# repeating characters
# # Example: length_of_longest_substring("abcabcbb") should return 3 (for "abc").


def length_of_longest_substring(s):
    max_len = 0

    for i in range(len(s)):
        sub = ""
        for j in range(i, len(s)):
            if s[j] not in sub:
                sub += s[j]
                max_len = max(max_len, len(sub))
            else:
                break

    return max_len

print(length_of_longest_substring("abcabcbb"))