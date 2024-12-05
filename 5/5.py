import os

# Read the entire file content
with open('input', 'r') as file:
    content = file.read()

# Split on double newline to separate sections
rules, printlists = content.split('\n\n')
sum = 0

toCorret = []

for pl in printlists.split('\n'):
    a = pl.split(',')
    middle = a[int((len(a) / 2))]
    flag = True
    for r in rules.split('\n'):
        rule = r.split('|')
        if rule[0] in a and rule[1] in a:
            if a.index(rule[0]) > a.index(rule[1]):
                flag = False
                toCorret.append(a)
                break              
            
    if flag:
        sum += int(middle)

sum2 = 0
print(sum)

def swapPlaces(brokenRules, t):
    for r in brokenRules:
        rule = r.split('|')
        if rule[0] in t and rule[1] in t and t.index(rule[0]) > t.index(rule[1]):
            t[t.index(rule[0])] , t[t.index(rule[1])] = t[t.index(rule[1])] , t[t.index(rule[0])]

for t in toCorret:
    brokenRules = rules.split('\n')
    for i in range(4):
        swapPlaces(brokenRules, t)
 
    middle = t[int((len(t) / 2))]
    sum2 += int(middle)

print(sum2)