#distance will be x coord diff + y cood diff since we can only move up and down

#need to figure out how to expand the array and check cols for no galaxies

import os
import numpy as np
from itertools import combinations



def GetExpansion(map, expansion):
    spaceMap = np.ones(map.shape, dtype=int)
    emptyRows = np.array([i for i, row in enumerate(map[:]) if not row.any()])
    emptyCols = np.array([i for i, col in enumerate(map.T[:]) if not col.any()])
    spaceMap[emptyRows] = expansion
    spaceMap[:, emptyCols] = expansion
    return spaceMap

def GetStarCoords(map, expansion):
    spaceMap = GetExpansion(map, expansion)
    galaxies = [(sum(spaceMap[:row, col]), sum(spaceMap[row, :col])) for row, col in np.argwhere(map) ]
    return galaxies

def ManhattanDistance(a, b):
    if len(a) != len(b):
        print("Error, mismatched tuples")
    
    return sum([abs(p - q) for p, q in zip(a, b)])

def GetDistances(galaxies):
    distance = np.int64()
    for galaxy1, galaxy2 in combinations(galaxies, 2):
        distance += ManhattanDistance(galaxy1, galaxy2)

    return distance



data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

fullInput = []
with open(data_file_path) as f:
    for line in f.readlines():
        line = line.strip('\n')
        fullInput.append([char for char in line])

fullInput = list(map(lambda row: [x == '#' for x in row], fullInput))

fullInput = np.array(fullInput)

galaxiesPart1 = GetStarCoords(fullInput, 2)
galaxiesPart2 = GetStarCoords(fullInput, 1000000)

print(GetDistances(galaxiesPart1))
print(GetDistances(galaxiesPart2))