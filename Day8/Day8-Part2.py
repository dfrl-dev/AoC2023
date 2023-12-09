import os

#recursive gcd -- return b % a, and a until a is 0 -- making b our greatest common divisor
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
 
#recursive LCM
def lcm(arr, idx):   
    # lcm(a,b) = (a*b/gcd(a,b))
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = lcm(arr, idx+1)
    return int(a*b/gcd(a,b))


data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

nodes = {}
directions = ''
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

nodesEndingInA = [key for key in nodes if key.endswith('A')]

#find the fastest route to the first node ending in Z for each node, then the lowest common multiple
#between all of them.
count = 0
allCounts = []
for node in nodesEndingInA:
    curr = node
    count = 0
    while not curr.endswith('Z'):
        for char in directions:
            if char == 'L':
                curr = nodes[curr][0]
                count+=1
                continue
            if char == 'R':
                curr = nodes[curr][1]
                count += 1
                continue
    allCounts.append(count)

print(lcm(allCounts, 0))
