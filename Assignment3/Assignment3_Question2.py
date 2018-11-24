#Comp Bio Fall 2018
#Assignment 3, Question 2
#SBU ID : 112027432
#Python 3.6

#Defining Variables
Edges = dict()
TopSort = list()
Path = list()

#Taking Graph Input
Graph = open("rosalind_ba5d.txt","r")
src  = int(Graph.readline())
sink = int(Graph.readline())

for edge in Graph:
	edge = edge.strip().split("->")
	
	a = int(edge[0])
	[b,wt] = edge[1].split(":")
	b = int(b)
	wt = int(wt)

	if a not in Edges.keys():
		Edges[a] = [[],0]

	if b not in Edges.keys():
		Edges[b] = [[],0]
	
	Edges[a][0].append((b,wt))
	Edges[b][1] += 1
Graph.close()

Edges1 = Edges.copy()

while len(Edges) > 0:
	Answer = []
	for key,value in Edges.items():
		if value[1] == 0:
			Answer.append(key)
			
	for key in Answer:
		for i,j in Edges[key][0]:
			Edges[i][1] -= 1
		del Edges[key]
	TopSort += Answer + []

m = max(Edges1.keys())
Distance = [float('-inf')]*(m+1)
BackPointer = [-1]*(m+1)
Distance[src] = 0

for x in TopSort:
	for i,j in Edges1[x][0]:
		if Distance[i] < Distance[x] + j:
			Distance[i] = Distance[x]+j
			BackPointer[i] = x

print(Distance[sink])

while BackPointer[sink] != -1:
	Path = [sink] + Path
	sink = BackPointer[sink]
Path = [sink] + Path

for i in Path:
	print(i,"->",sep="",end="")