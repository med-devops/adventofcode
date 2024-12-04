import os 
import numpy as np

f = open('input', 'r').readlines()
f = [line.strip() for line in f]  # Remove newlines and create list of strings

total = 0

# Get dimensions from input
height = len(f)
width = len(f[0]) if height > 0 else 0

# Convert to numpy array
matrix = np.array([list(line) for line in f])
print("Input matrix:")
print(matrix)

word = "XMAS"
word2 = "SAMX"
vertical = []
for i in range(width):
    line = ""
    for l in f:
        line = line + l[i]
    vertical.append(line)

def check(f):
    count = 0
    for l in f:
        i = 0
        i2 = 0
        for ch in l:
            if ch == word[i]:
                i += 1
                if i == len(word) - 1:
                    count += 1
                    i = 0
            if ch == word2[i2]:
                i2 += 1
                if i2 == len(word2) - 1:
                    count += 1
                    i2 = 0    
    return count                    
total += check(f)
total += check(vertical)
total += check(matrix)
    
print(total)
