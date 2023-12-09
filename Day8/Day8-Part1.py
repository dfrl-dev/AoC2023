import os
from collections import Counter

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

nodes = {}
directions = ''

firstKey = ''
with open(data_file_path) as f:
    for i, line in enumerate(f):
        if i == 0:
            directions = line.strip('\n')
            continue

        if i == 1:
            continue
        
        sides = line.split('=')
        node = sides[0].strip()

        if i == 2:
            firstKey = node
        branches = sides[1].strip(' ()\n')
        left = branches.split(',')[0].strip()
        right = branches.split(',')[1].strip()

        nodes[node] = (left, right)


curr = 'AAA'
count = 0
while curr != 'ZZZ':
    for char in directions:
        if char == 'L':
            curr = nodes[curr][0]
            count += 1
            continue
        if char == 'R':
            curr = nodes[curr][1]
            count += 1
            continue

print(count)