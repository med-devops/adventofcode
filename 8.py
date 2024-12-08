import os
import itertools

with open('8.in', 'r') as file:
    content = file.read().strip().splitlines()


def get_all_arrangements(items, length):

    arrangements = list(itertools.permutations(items, 2))
    return [list(p) for p in arrangements]

antenaDict = {}
for row in range(len(content)):
    for col in range(len(content[row])):
        if content[row][col] != ".":
            if content[row][col] in antenaDict:
                antenaDict[content[row][col]].append([row, col])
            else:
                antenaDict[content[row][col]] = [[row, col]]
antinodes = []
for key in antenaDict:
    print(key)
    values = antenaDict[key]
    print(values)
    combinations = get_all_arrangements(values, 2)
    for combination in combinations:
        if combination in [comb[::-1] for comb in combinations]:
            combinations.remove(combination)
    for combination in combinations:
        print(combination)
        if combination[0][0] == combination[1][0] and combination[0][1] == combination[1][1]:
            continue
        xChange = abs(combination[0][1] - combination[1][1])
        yChange = abs(combination[0][0] - combination[1][0])
        if combination[0][1] > combination[1][1]:
            antinode1X = combination[1][1] - xChange
            antinode2X = combination[0][1] + xChange
        else:
            antinode1X = combination[0][1] - xChange
            antinode2X = combination[1][1] + xChange
        if combination[0][0] > combination[1][0]:
            antinode1Y = combination[1][0] - yChange
            antinode2Y = combination[0][0] + yChange
        else:
            antinode1Y = combination[0][0] - yChange
            antinode2Y = combination[1][0] + yChange
        if antinode1X > 0 and antinode1X <= len(content[0]) and antinode1Y > 0 and antinode1Y <= len(content):
            antinodes.append([antinode1X, antinode1Y])
        if antinode2X > 0 and antinode2X <= len(content[0]) and antinode2Y > 0 and antinode2Y <= len(content):
            antinodes.append([antinode2X, antinode2Y])
        


uniqueantinodes = []
for node in antinodes:
    if node not in uniqueantinodes:
        uniqueantinodes.append(node)
print(len(uniqueantinodes))

print(antinodes)