# Write a Python function that converts a CamelCase string into a snake_case string
# using re.sub(). The solution should insert an underscore before every uppercase
# letter (except the first one) and convert the entire string to lowercase. Example Input:
# "thisIsAConversionExample"
# Expected Output: "this_is_a_conversion_example"

import re

def camel_to_snake(s):
    result = re.sub(r'([A-Z])', r'_\1', s)   #re.sub(pattern, replacement, string)
    return result.lower()

text = "thisIsAConversionExample"
print(camel_to_snake(text))