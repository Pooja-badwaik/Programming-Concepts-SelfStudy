# 2. Given a string s, return the longest palindromic substring in s.
# Example: For "babad", the answer is "bab" (or "aba").


s = "babad"
longest = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub

print("Longest palindrome:", longest)