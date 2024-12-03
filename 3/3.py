import os 
import re

f = open('input', 'r').read()
pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, f)

sum = 0 
for m in matches:
    sum +=int(m[0]) * int(m[1])

print(sum)
sum2 = 0
dos = f.split('do()')
for d in dos:
    d = d.split('don')[0]
    match2 = re.findall(pattern, d)
    for m in match2:
        sum2 += int(m[0]) * int(m[1])

print(sum2)