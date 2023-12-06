import os
import re

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

input = []
with open(data_file_path) as f:
    for line in f.readlines():
        line.strip('\n')
        current = ''
        for char in line[line.index(':') + 1 :]:
            if char.isnumeric():
                current += char
        
        input.append(int(current))


for i in range(0, int(len(input)/2)):
    pairIdx = int(len(input)/2 + i)

    time = input[i]
    distance = input[pairIdx]

    minWin = 0
    maxWin = 0

    #optimize to find the range of winning numbers, instead of checking every single one.
    for j in range(1, time):
        travelled = j * (time - j)
        if(travelled > distance):
            minWin = j
            break
    
    for k in range(time, 0, -1):
        travelled = k * (time - k)
        if travelled > distance:
            maxWin = k
            break
    
    numWins = maxWin - minWin + 1
    print(numWins)






