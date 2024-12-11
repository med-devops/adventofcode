import os
import itertools

with open('9.in', 'r') as file:
    content = file.read()

file = ""
counter = 0
for i in range(len(content)):
    if i == 0:
        for j in range(int(content[i])):
            file += str(counter)
    if i % 2 == 0:
        for j in range(int(content[i])):
            file += "."
    else:
        for j in range(int(content[i])):
            file += str(counter)
    counter += 1

reverse = file[::-1]
for i in range(len(reverse)): 
    if reverse[i] == ".":
        reverse = reverse[:i]+reverse[i+1:]

print(file.split(".")[-1])
# for i in range(len(file)):
#     if file[i] == ".":
#         file[i] = reverse[-1]
#         reverse = reverse[:-1]
#     else:
#         continue

            