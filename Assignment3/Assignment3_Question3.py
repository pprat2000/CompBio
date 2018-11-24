#Comp Bio Fall 2018
#Assignment 3, Question 3
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

print(word1)
print(word2)
n = len(word1)
m = len(word2)

if m == 0:
    print(n)
if n == 0:
    print(m)

Grid = [[0 for i in range(n)] for i in range(m)]

if word1[0] != word2[0]:
    Grid[0][0] = 1

for i in range(1,n):
    if word2[0] == word1[i]:
        if Grid[0][i-1] == i:
            Grid[0][i] = i
        else:
            Grid[0][i] = i+1
    else:
        Grid[0][i] = Grid[0][i-1]+1
        
for i in range(1,m):
    if word1[0] == word2[i]:
        if Grid[i-1][0] == i:
            Grid[i][0] = i
        else:
            Grid[i][0] = i+1
    else:
        Grid[i][0] = Grid[i-1][0]+1

for i in range(1,m):
    for j in range(1,n):
        Grid[i][j] = min(Grid[i-1][j],Grid[i][j-1],Grid[i-1][j-1]) +  1
        if word1[j] == word2[i]:
        	Grid[i][j] = min(Grid[i][j],Grid[i-1][j-1])
for i in Grid:
    print(i)