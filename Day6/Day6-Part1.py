import os
import re

data_file_path = os.path.join(os.path.dirname(__file__), "testInput.txt")

input = []
with open(data_file_path) as f:
    for line in f.readlines():
        line.strip('\n')
        current = ''
        for char in line[line.index(':') + 1 :]:
            if char == ' ' and current != '':
                input.append(int(current))
                current = ''
                continue
            if char.isnumeric():
                current += char
        
        input.append(int(current))

waysToWin = []
for i in range(0, int(len(input)/2)):
    pairIdx = int(len(input)/2 + i)

    time = input[i]
    distance = input[pairIdx]

    winningCombos = 0

    for j in range(1, time):
        travelled = j * (time - j)
        if(travelled > distance):
            winningCombos += 1
    
    waysToWin.append(winningCombos)

print(waysToWin)

total = waysToWin[0]

for i in range(1, len(waysToWin)):
    total *= waysToWin[i]

print(total)

