import os
import re     


data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

input = []
with open(data_file_path) as f:
    for line in f:
        input.append(line.strip('\n'))

seeds = []
seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemp = []
tempToHumidity = []
humidityToLocation = []

mapNumber = 0
for i, line in enumerate(input):
    if i == 0:
        currentNumber = ""
        for char in line[line.index(':') + 2:]:
            if(char == ' '):
                seeds.append(currentNumber)
                currentNumber = "" 
            else:
                currentNumber += char
            
        seeds.append(currentNumber)
        continue
    
    if ':' in line:
        mapNumber += 1
        continue

    if line == '':
        continue

    vals = line.split(' ')

    if mapNumber == 1:
        seedToSoil.append((int(vals[0]), int(vals[1]), int(vals[2])))
    elif mapNumber == 2:
        soilToFertilizer.append((int(vals[0]), int(vals[1]), int(vals[2])))
    elif mapNumber == 3:
        fertilizerToWater.append((int(vals[0]), int(vals[1]), int(vals[2])))
    elif mapNumber == 4:
        waterToLight.append((int(vals[0]), int(vals[1]), int(vals[2])))
    elif mapNumber == 5:
        lightToTemp.append((int(vals[0]), int(vals[1]), int(vals[2])))
    elif mapNumber == 6:
        tempToHumidity.append((int(vals[0]), int(vals[1]), int(vals[2])))
    elif mapNumber == 7:
        humidityToLocation.append((int(vals[0]), int(vals[1]), int(vals[2])))



locations = []
minLocation = 0

for i in range(0, len(seeds), 2):
    seedStart = int(seeds[i])
    seedRange = int(seeds[i + 1])
    skip = int(seeds[i+ 1])
    nextSeed = seedStart
    while nextSeed <= seedStart + seedRange:
        res = nextSeed
        for i, map in enumerate(seedToSoil):
            if map[1] <= res < (map[1] + map[2]): #seed is in range of the map
                skip = min(skip, map[1] + map[2] - res)
                res += (map[0] - map[1])
                if skip <= 0:
                    skip = 1
                break
        for i, map in enumerate(soilToFertilizer):
            if map[1] <= res < (map[1] + map[2]): #seed is in range of the map
                skip = min(skip, map[1] + map[2] - res)
                res += (map[0] - map[1])
                if skip <= 0:
                    skip = 1
                break
        for i, map in enumerate(fertilizerToWater):
            if map[1] <= res < (map[1] + map[2]): #seed is in range of the map
                skip = min(skip, map[1] + map[2] - res)
                res += (map[0] - map[1])
                if skip <= 0:
                    skip = 1
                break
        for i, map in enumerate(waterToLight):
            if map[1] <= res < (map[1] + map[2]): #seed is in range of the map
                skip = min(skip, map[1] + map[2] - res)
                res += (map[0] - map[1])
                if skip <= 0:
                    skip = 1                
                break
        for i, map in enumerate(lightToTemp):
            if map[1] <= res < (map[1] + map[2]): #seed is in range of the map
                skip = min(skip, map[1] + map[2] - res)
                res += (map[0] - map[1])
                if skip <= 0:
                    skip = 1                
                break
        for i, map in enumerate(tempToHumidity):
            if map[1] <= res < (map[1] + map[2]): #seed is in range of the map
                skip = min(skip, map[1] + map[2] - res)
                res += (map[0] - map[1])
                if skip <= 0:
                    skip = 1                
                break
        for i, map in enumerate(humidityToLocation):
            if map[1] <= res < (map[1] + map[2]): #seed is in range of the map
                skip = min(skip, map[1] + map[2] - res)
                res += (map[0] - map[1])
                if skip <= 0:
                    skip = 1                
                break

        locations.append(res)
        nextSeed += skip #max skip is calculated at each translation, and we apply it each time around
        skip = seedRange - nextSeed + seedStart #reset skip to be range - seed + start, if it's outside of the current range of seeds, move to next seed.

minLocation = min(locations)

print(minLocation)





