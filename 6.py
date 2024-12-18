import os

# Read the entire file content
with open('input', 'r') as file:
    content = file.readlines()


for i in range(len(content)):
    if "^" in content[i]:
        yposition = i
        break
for i in range(len(content[yposition])):
    if content[yposition][i] == "^":
        xposition = i
        break
print(xposition, yposition)    

direction = "up"
dict = {
    "right": [1,0],
    "down": [0,1],
    "left": [-1,0],
    "up": [0,-1]
}
steps = []
while xposition < len(content[yposition]) and xposition >= 0 and yposition < len(content) and yposition >= 0:
    move = dict[direction]
    if xposition + move[0] <= len(content[yposition]) and xposition + move[0] >= 0 and yposition + move[1] < len(content) and yposition + move[1] >= 0:
        if content[yposition + move[1]][xposition + move[0]] != "#":
            xposition += move[0]
            yposition += move[1]
            steps.append([yposition,xposition])
        else:
            if direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "up"
            elif direction == "up":
                direction = "right"
    else:
        break


done = []
count = 0
for step in steps:
    if step not in done:
        done.append(step)
        count += 1
print(count+1)


#############################
def part2(xposition, yposition, content):
    flag = False
    direction = "up"
    dict = {
    "right": [1,0],
    "down": [0,1],
    "left": [-1,0],
    "up": [0,-1] }
    steps = []
    while xposition < len(content[yposition]) and xposition >= 0 and yposition < len(content) and yposition >= 0:
        move = dict[direction]
        if xposition + move[0] <= len(content[yposition]) and xposition + move[0] >= 0 and yposition + move[1] < len(content) and yposition + move[1] >= 0:
            if content[yposition + move[1]][xposition + move[0]] != "#":
                xposition += move[0]
                yposition += move[1]
                if [yposition,xposition,direction] in steps:
                    flag = True
                    break
                else:
                    steps.append([yposition,xposition,direction])
            else:
                if direction == "right":
                    direction = "down"
                elif direction == "down":
                    direction = "left"
                elif direction == "left":
                    direction = "up"
                elif direction == "up":
                    direction = "right"
        else:
            break
    return flag

counter = 0
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == "#":
            continue
        else:
            testcontent = content.copy()
            testcontent[i] = testcontent[i][:j] + "#" + testcontent[i][j+1:]
            if part2(xposition, yposition, testcontent):
                counter += 1
            


        