import os
import itertools

with open('10.in', 'r') as file:
    content = file.read().strip().splitlines()
global sum
sum = 0
def findTrail(j, i, content):
    value = int(content[j][i])
    if value == 9:
        sum += 1
    if j > 0:
        if int(content[j-1][i]) == value + 1:
            findTrail(j-1, i, content) 
    if j < len(content) -1:
        if int(content[j+1][i]) == value + 1:
            findTrail(j+1, i, content)
    if i > 0:
        if int(content[j][i-1]) == value + 1:
            findTrail(j, i-1, content)
    if i < len(content[0]) -1:
        if int(content[j][i+1]) == value + 1:
            findTrail(j, i+1, content)



for j in range(len(content)):
    for i in range(len(content[0])):
        if content[j][i] == "0":
            findTrail(j, i, content)

print(sum)