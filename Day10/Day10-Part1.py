import os
import numpy as np


def GetDirections(x, y, fullInput):
    validDirections = []
    if x > 0:
        #look up
        if fullInput[x - 1][y] == '|' or fullInput[x - 1][y] == '7' or fullInput[x - 1][y] =='F':
            validDirections.append('NORTH')        
    if y > 0:
        #look left
        if fullInput[x][y - 1] == '-' or fullInput[x][y - 1 ] == 'L' or  fullInput[x][y - 1] == 'F':
            validDirections.append('WEST')
    
    if y < len(fullInput[0]) - 1:
        if fullInput[x][y + 1] == '-' or fullInput[x][y + 1] == 'J' or fullInput[x][y + 1] == '7':
            validDirections.append('EAST')

    if x < len(fullInput) - 1:
        if fullInput[x + 1][y] == '|' or fullInput[x + 1][y] == 'J' or fullInput[x + 1][y] == 'L':
            validDirections.append('SOUTH')

    return validDirections

def GetIndex(x, y, direction):
    if direction == 'NORTH':
        x -= 1
    elif direction == 'SOUTH':
        x += 1
    elif direction == 'EAST':
        y += 1
    elif direction == 'WEST':
        y -= 1

    return x, y

def GetStep(currX, currY, prevX, prevY, char):
    newX = -1
    newY = -1
    if char == 'F':
        #entering from below, so now we move right
        if currX - prevX == -1:
            newY = currY + 1
            newX = currX
        else:
            newX = currX + 1
            newY = currY
        
    elif char == "|":
        if currX - prevX == 1:
            newX = currX + 1
            newY = currY
        else:
            newX = currX - 1
            newY = currY
        
    elif char == "-":
        if currY - prevY == 1:  #entering from left
            newY = currY + 1
            newX = currX
        else:
            newY = currY - 1
            newX = currX
        
    elif char == 'L':
        if currX - prevX == 1: #enter from top
            newX = currX
            newY = currY + 1
        else:
            newX = currX - 1
            newY = currY
        
    elif char == '7':
        if currY - prevY == 1:
            newX = currX + 1
            newY = currY
        else:
            newX = currX
            newY = currY - 1
        
    elif char == 'J':
        if currX - prevX == 1:
            newX = currX
            newY = currY - 1
        else:
            newX = currX - 1
            newY = currY
        

    return newX, newY

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

fullInput = []
with open(data_file_path) as f:
    for line in f.readlines():
        line = line.strip('\n')
        fullInput.append([x for x in line])


startX = -1
startY = -1

for row, line in enumerate(fullInput):
    for col, char in enumerate(line):
        if char == 'S':
            startX = row
            startY = col


validDirections = GetDirections(startX, startY, fullInput)

found = False

prevX1 = startX
prevY1 = startY
prevX2 = startX
prevY2 = startY

dir1 = validDirections[0]
dir2 = validDirections[1]

currX1, currY1 = GetIndex(prevX1, prevY1, dir1)
currX2, currY2 = GetIndex(prevX2, prevY2, dir2)

steps = 1

##need to take into account current pipe, or might get false direction positives
while not found:
    currChar1 = fullInput[currX1][currY1]
    currChar2 = fullInput[currX2][currY2]
    fullInput[currX1][currY1] = '*'
    fullInput[currX2][currY2] = '*'

    movX1, movY1 = GetStep(currX1, currY1, prevX1, prevY1, currChar1)
    movX2, movY2 = GetStep(currX2, currY2, prevX2, prevY2, currChar2)

    prevX1 = currX1
    prevY1 = currY1
    prevX2 = currX2
    prevY2 = currY2

    currX1 = movX1
    currY1 = movY1
    currX2 = movX2
    currY2 = movY2

    steps += 1

    if currX1 == currX2 and currY1 == currY2:
        found = True

print(steps)