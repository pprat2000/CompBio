#Comp Bio Fall 2018
#Assignment 3, Question 1
#SBU ID : 112027432
#Python 3.6

#Defining Variables
Edges = {}
Path = list()

#Taking Graph Input
with open("rosalind_ba5n.txt","r") as Graph:
	for edge in Graph:
		edge = edge.strip().split(' ')
		edge[-1] = edge[-1].split(',')
		
		a = int(edge[0])
		
		#One list to keep track of where edges point
		#Second value to keep track of number of incoming edges
		if a not in Edges.keys():
			Edges[a] = [[],0]

		for b in edge[-1]:
			b = int(b)
			if b not in Edges.keys():
				Edges[b] = [[],0]
			
			Edges[a][0].append(b)
			Edges[b][1] += 1
Graph.close()

while len(Edges) > 0:
	Answer = []
	for key,value in Edges.items():
		if value[1] == 0:
			Answer.append(key)
			
	for key in Answer:
		print(",",key,sep=" ",end="")
		for i in Edges[key][0]:
			Edges[i][1] -= 1
		del Edges[key]