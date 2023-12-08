import os
from collections import Counter

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

fullInput = []
with open(data_file_path) as f:
    for line in f.readlines():
        fullInput.append(line.strip('\n'))

#dict for easy string sorting
cardValues = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 15
}

#lowest (high card), to highest (5 of a kind)
handTypes = [[],[],[],[],[],[],[]]

for line in fullInput:
    hand = line.split(' ')[0]
    frequencies = Counter(hand)

    if 5 in frequencies.values():
        handTypes[6].append(line)
    elif 4 in frequencies.values():
        handTypes[5].append(line)
    elif 3 in frequencies.values() and 2 in frequencies.values():
        handTypes[4].append(line)
    elif 3 in frequencies.values():
        handTypes[3].append(line)
    elif sum(value == 2 for value in frequencies.values()) == 2:
        handTypes[2].append(line)
    elif sum(value == 2 for value in frequencies.values()) == 1:
        handTypes[1].append(line)
    else:
        handTypes[0].append(line)

for j, type in enumerate(handTypes):
    type.sort(key=lambda x: [cardValues.get(c) for c in x])

totalWinnings = 0
rank = 1
for combination in handTypes:
    for hand in combination:
        handValue = hand.split(' ')
        totalWinnings += int(hand.split(' ')[1]) * rank
        rank+=1

print(totalWinnings)