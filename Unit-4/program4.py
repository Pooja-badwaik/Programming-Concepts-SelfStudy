# 4. Given a sample log file line, use re.split() to divide the string into a list containing the
# timestamp, log_level, message, and details. The separators are consistent patterns of
# brackets, spaces, and hyphens.
# Example Input: "[2025-12-17 10:00:00]- ERROR- User login failed: Invalid credentials"
# Expected Output: ['2025-12-17 10:00:00', 'ERROR', 'User login failed', 'Invalid
# credentials']


def func():


    import re

    log = "[2025-12-17 10:00:00]- ERROR- User login failed: Invalid credentials"

    parts = re.split(r"\[|\]- |: ", log)
    parts = [p for p in parts if p]   # remove empty strings

    print(parts)



func()