import os

data_file_path = os.path.join(os.path.dirname(__file__), "tinput.txt")

fullInput = []
with open(data_file_path) as f:
    for line in f.readlines():
        line = line.strip('\n')
        fullInput.append([int(x) for x in line.split(' ')])
sequences = []
for sequence in fullInput:
    curr = sequence
    subsequences = []
    subsequences.append(sequence)

    newSeq = curr
    while not all(v == 0 for v in newSeq):
        curr = newSeq
        newSeq = []
        for i in range(0, len(curr) - 1, 1):
            newSeq.append(int(curr[i + 1]) - int(curr[i]))
        
        subsequences.append(newSeq)

    sequences.append(subsequences)

predictions = []

for sequence in sequences:
    for i in range(len(sequence) - 1, 0, -1):
        newVal = sequence[i - 1][len(sequence[i])-1] + sequence[i][len(sequence[i])-1]
        sequence[i - 1].append(newVal)
    predictions.append(sequence[0][len(sequence[0])-1])



total = sum(predictions)

print(total)

