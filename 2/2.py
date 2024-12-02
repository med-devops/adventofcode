import os 

f = open('input', 'r').read().splitlines()

sum = 0

sum2 = 0

def ascend(a):
    return all(a[i] < a[i + 1] and 1 <= a[i+1] - a[i] and a[i+1] - a[i] <= 3  for i in range(len(a) - 1))

def descend(a):
    return all(a[i] > a[i + 1] and 1 <= a[i] - a[i+1] and a[i] - a[i+1] <= 3 for i in range(len(a) - 1))

secondrun = []
for l in f:
    a = [int(x) for x in l.split()]
    if ascend(a) or descend(a):
        sum += 1
    else:
        secondrun.append(a)

for l2 in secondrun:
    for i in range(len(l2)):
        # Create new list without element at index i
        a = l2[:i] + l2[i+1:]
        if ascend(a) or descend(a):
            sum2 += 1
            break



print(sum)
print(sum2+sum)