import os 

f = open('input', 'r').read().splitlines()

l1 = []
l2 = []
sum = 0
sum2 = 0 
for l in f:
    lout = l.split()
    l1.append(int(lout[0]))
    l2.append(int(lout[1]))

for i in range(len(l1)):
    sum2 += l2.count(l1[i]) * l1[i]


for i in range(len(l1)):
    sum += abs(min(l1) - min(l2))
    l1.remove(min(l1))
    l2.remove(min(l2))

print(sum)
print(sum2)