import os
import re

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

input = []
with open(data_file_path) as f:
    for line in f:
        input.append(line.strip('\n'))

toSum = []
notParts = []
currentNumber = ''
isPartNumber = False
for i, row in enumerate(input):   
    for j, col in enumerate(row):
        if col == '*':
            numMatches = 0
            matches = [''] * 6
            #check left of gear
            if j > 0 and row[j-1].isnumeric():
                index = j - 1
                while index > 0 and row[index].isnumeric():
                     matches[numMatches] = row[index] + matches[numMatches]
                     index -= 1
                numMatches += 1

            #check right of number
            if j < len(row) - 1 and row[j + 1].isnumeric():
                index = j + 1
                while index < len(row) and row[index].isnumeric():
                    matches[numMatches] += row[index]
                    index += 1
                numMatches += 1

            #check above number
            matchTop = False
            if i > 0 and input[i - 1][j].isnumeric():
                index = j
                doneCheck = False
                while not doneCheck:
                    matches[numMatches] += input[i - 1][index]
                    if index > 0:
                        negIndex = index - 1
                        while input[i - 1][negIndex].isnumeric():
                             matches[numMatches] = input[i - 1][negIndex] + matches[numMatches] #check left and append to front
                             negIndex -= 1
                    if index < len(row) - 1:
                         posIndex = index + 1
                         while input[i - 1][posIndex].isnumeric():
                              matches[numMatches] += input[i - 1][posIndex]
                              posIndex += 1
                    doneCheck = True
                numMatches += 1  
                matchTop = True              

            matchBelow = False
            #check below number
            if i < len(input) - 1 and input[i + 1][j].isnumeric():
                index = j
                doneCheck = False
                while not doneCheck:
                    matches[numMatches] += input[i + 1][index]
                    if index > 0:
                        negIndex = index - 1
                        while input[i + 1][negIndex].isnumeric():
                             matches[numMatches] = input[i + 1][negIndex] + matches[numMatches] #check left and append to front
                             negIndex -= 1
                    if index < len(row) - 1:
                         posIndex = index + 1
                         while input[i + 1][posIndex].isnumeric():
                              matches[numMatches] += input[i + 1][posIndex]
                              posIndex += 1
                    doneCheck = True
                numMatches += 1  
                matchBelow = True

            if not matchTop:
                #check up left diag
                if i > 0 and j > 0 and input[i - 1][j - 1].isnumeric():
                    index = j - 1
                    while input[i - 1][index].isnumeric():
                        matches[numMatches] = input[i - 1][index] + matches[numMatches]
                        index -= 1
                    numMatches += 1
                
                            #check up right diag
                if i > 0 and j < len(row) - 1 and input[i - 1][j + 1].isnumeric():
                    index = j + 1
                    while input[i - 1][index].isnumeric():
                        matches[numMatches] += input[i - 1][index]
                        index += 1
                    numMatches += 1

            if not matchBelow:
                #check down left diag
                if i < len(input) - 1 and j > 0 and input[i + 1][j - 1].isnumeric():
                    index = j - 1
                    while input[i + 1][index].isnumeric():
                        matches[numMatches] = input[i + 1][index] + matches[numMatches]
                        index -= 1
                    numMatches += 1

                #check check down right dig
                if i < len(input) - 1 and j < len(row) - 1 and input[i + 1][j + 1].isnumeric():
                    index = j + 1
                    while input[i + 1][index].isnumeric():
                        matches[numMatches] += input[i + 1][index]
                        index += 1
                    numMatches += 1

            if numMatches == 2:
                toSum.append(int(matches[0]) * int(matches[1]))

total = 0

for partNumber in toSum:
     total += int(partNumber)

print(total)





        







    
    