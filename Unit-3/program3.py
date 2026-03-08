# 3. Given a string s consisting of opening and closing parenthesis '(' and ')', find the
# length of the longest valid parenthesis substring. A valid parenthesis substring is one
# where every opening bracket '(' has a corresponding closing bracket ')' in the correct
# order.
# Examples: Input: s = "())"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Input: s = "(()())"
# Output: 6





s = "(()())"
max_len = 0

for i in range(len(s)):
    open_c = 0
    close_c = 0
    for j in range(i, len(s)):
        if s[j] == "(":
            open_c += 1
        else:
            close_c += 1
        
        if open_c == close_c:
            max_len = max(max_len, open_c + close_c)
        elif close_c > open_c:
            break

print("Longest valid parentheses length:", max_len)