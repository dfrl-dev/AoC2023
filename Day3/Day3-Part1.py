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
        if col.isnumeric():
            currentNumber += col

            #check left of number
            if j > 0 and not row[j-1].isnumeric() and not row[j-1] == '.':
                isPartNumber = True

            #check right of number
            if j < len(row) - 1 and not row[j + 1].isnumeric() and not row[j+1] == '.':
                isPartNumber = True

            #check above number
            if i > 0 and not input[i - 1][j].isnumeric() and not  input[i - 1][j] == '.':
                isPartNumber = True

            #check below number
            if i < len(input) - 1 and not input[i + 1][j].isnumeric() and not  input[i + 1][j] == '.':
                isPartNumber = True

            #check up left diag
            if i > 0 and j > 0 and not input[i - 1][j - 1].isnumeric() and not input [i - 1][j - 1] == '.':
                isPartNumber = True

            #check down left diag
            if i < len(input) - 1 and j > 0 and not input[i + 1][j - 1].isnumeric() and not input[i + 1][j - 1] == '.':
                isPartNumber = True

            #check up right diag
            if i > 0 and j < len(row) - 1 and not input[i - 1][j + 1].isnumeric() and not input [i - 1][j + 1] == '.':
                isPartNumber = True

            #check check down right dig
            if i < len(input) - 1 and j < len(row) - 1 and not input[i + 1][j + 1].isnumeric() and not input[i + 1][j + 1] == '.':
                isPartNumber = True

            if j == len(row) - 1 or (j < len(row) - 1 and not row[j + 1].isnumeric()):
                        if isPartNumber:
                            toSum.append(currentNumber)
                            currentNumber = ''
                            isPartNumber = False
                        else:
                             notParts.append(currentNumber)
                             currentNumber = ''

total = 0

for partNumber in toSum:
     total += int(partNumber)


print(toSum)
print('notPArts: ', notParts)
print(total)





        







    
    