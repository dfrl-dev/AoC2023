import os
import re

data_file_path = os.path.join(os.path.dirname(__file__), "Day2.txt")


inventory = {
    'red': 12,
    'blue': 14,
    'green': 13
}

with open(data_file_path) as f:
    input = f.readlines()

games = []


for i, line in enumerate(input):
    gameNumber = i + 1
    subgames = line[line.index(':') + 2:].split(';')
    minRed = 0
    minGreen = 0
    minBlue = 0
    for game in subgames:
        blues = re.findall(r'(\d+) blue', game)
        greens = re.findall(r'(\d+) green', game)
        reds = re.findall(r'(\d+) red', game)

        if(len(blues) == 0):
            blues.append(0)
        
        if(len(greens) == 0):
            greens.append(0)
        
        if(len(reds) == 0):
            reds.append(0)

        if int(reds[0]) > minRed:
            minRed = int(reds[0])
        if int(greens[0]) > minGreen:
            minGreen = int(greens[0])
        if int(blues[0]) > minBlue:
            minBlue = int(blues[0])
    
    powah = minRed * minGreen * minBlue
    games.append(powah)

total = 0
for val in games:
    total += val

print(total)

