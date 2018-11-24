#Comp Bio Fall 2018
#Assignment 3, Question 5
#SBU ID : 112027432
#Python 3.6


i = 0
word1 = ""
word2 = ""

with open("rosalind_edit.txt",'r') as stringFile:
	for line in stringFile:
		if line[0] == '>':
			i += 1
			continue
		if i == 1:
			word1 += line.strip()
		if i == 2:
			word2 += line.strip()

n = len(word1)
m = len(word2)

if m == 0:
    print(n)
if n == 0:
    print(m)

Grid = [[0 for i in range(n+1)] for i in range(m+1)]
BestWayToReach = [[0 for i in range(n+1)] for i in range(m+1)]

Grid[0][0] = 0
BestWayToReach[0][0] = 1

for i in range(1,n+1):
    BestWayToReach[0][i] = 1
    Grid[0][i] = Grid[0][i-1]+1
        
for i in range(1,m+1):
    BestWayToReach[i][0] = 1
    Grid[i][0] = Grid[i-1][0]+1

for i in range(1,m+1):
    for j in range(1,n+1):
        if word2[i-1] == word1[j-1]:
            Grid[i][j] = Grid[i-1][j-1]
            BestWayToReach[i][j] += BestWayToReach[i-1][j-1]
            if Grid[i][j] == Grid[i-1][j]+1:
                BestWayToReach[i][j] += BestWayToReach[i-1][j]
            if Grid[i][j] == Grid[i][j-1]+1:
                BestWayToReach[i][j] += BestWayToReach[i][j-1]
            continue
        x = min(Grid[i-1][j],Grid[i][j-1],Grid[i-1][j-1])
        if x == Grid[i-1][j]:
            BestWayToReach[i][j] += BestWayToReach[i-1][j]
        if x == Grid[i][j-1]:
            BestWayToReach[i][j] += BestWayToReach[i][j-1]
        if x == Grid[i-1][j-1]:
            BestWayToReach[i][j] += BestWayToReach[i-1][j-1]
        Grid[i][j] = x+1

for i in Grid:
    print(i)
print("--------------------------")
for i in BestWayToReach:
    print(i)