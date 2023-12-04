import os
import re

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

input = []
with open(data_file_path) as f:
    for line in f:
        input.append(line.strip('\n'))

total = 0
totalCards = dict.fromkeys(range(len(input)), 1)
for i, line in enumerate(input):
    cardValue = 0
    numMatches = 0
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


    j = 1
    while j <= numMatches:
        totalCards[i + j] += totalCards[i]
        j += 1

print(totalCards)    
total = sum(totalCards.values())

print(total)
