import os
import itertools

with open('7.in', 'r') as file:
    content = file.readlines()
eqations = []
for line in content:
    temp = line.strip().split(': ')
    temp2 = [int(i) for i in temp[1].split(' ')]
    eqations.append([int(temp[0]), temp2])


operands = [0,1]


def get_all_arrangements(items, length):

    arrangements = list(itertools.product(items, repeat=length))
    return [list(p) for p in arrangements]

total_p1 = 0
for eq in eqations:
    value = eq[0]
    numbers = eq[1]
    arrs = get_all_arrangements(operands, len(numbers) -1)
    for a in arrs:
        for i in range(len(numbers)):
            if i == 0:
                sum = numbers[i]
            else:
                if a[i-1] == 0:
                    sum += numbers[i]
                else:
                    sum *= numbers[i]
        if sum == value:
            total_p1 +=sum
            break

total_p2 = 0
operands2 = [0,1,2]
for eq in eqations:
    value = eq[0]
    numbers = eq[1]
    arrs = get_all_arrangements(operands2, len(numbers) -1)
    for a in arrs:
        for i in range(len(numbers)):
            if i == 0:
                sum = numbers[i]
            else:
                if a[i-1] == 0:
                    sum += numbers[i]
                elif a[i-1] == 1:
                    sum *= numbers[i]
                else:
                    sum = int(str(sum) + str(numbers[i]))
                
        if sum == value:
            total_p2 +=sum
            break


print(total_p1)
print(total_p2)

        