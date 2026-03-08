# 1. Write a Python program to check that a string contains only a certain set of
# characters (in this case a-z, A-Z and 0-9)




s = input("Enter string: ")

if s.isalnum():
    print("String contains only a-z, A-Z, 0-9")
    print("Hence,It is a valid ")
else:
    print("String contains other characters")
    print("Hence,It is not  valid ")