import os
import re

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

input = []
with open(data_file_path) as f:
    for line in f:
        input.append(line.strip('\n'))

total = 0
for i, line in enumerate(input):
    cardValue = 0
    numMatches = -1
    winningNumbersString = line[line.index(':') + 1 : line.index('|')]

    ourNumbersString = line[line.index('|') + 1 :]

    winningNumbers = winningNumbersString.split(' ')
    ourNumbers = ourNumbersString.split(' ')

    winningNumbers = list(filter(None, winningNumbers))
    ourNumbers = list(filter(None, ourNumbers))

    for number in ourNumbers:
        for win in winningNumbers:
            if number == win:
                numMatches += 1
    
    if numMatches >= 0:
        cardValue = pow(2, numMatches)
    
    total += cardValue

print(total)
