# 2. Write a Python program to remove leading zeros from an IP address.
# Input: 216.08.094.196
# Output: 216.8.94.196



ip = "216.08.094.196"

parts = ip.split(".")

for i in range(len(parts)):
    parts[i] = str(int(parts[i]))

new_ip = ".".join(parts)

print(new_ip)