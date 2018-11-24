#Comp Bio Fall 2018
#Assignment 2, Question 2
#SBU ID : 112027432

#Defining Variables
Edges = {}
Paths = []
Out,In,Visited = 0,1,2

#Function to check if a node is 1-1
def isNodeOneToOne(node):
	if len(Edges[node][In]) == 1 and len(Edges[node][Out]) == 1:
		return True
	else:
		return False

#Taking Graph Input
with open("rosalind_ba3m.txt","r") as Graph:
	for edge in Graph:
		edge = edge.strip()

		x = edge.find('-')
		a = int(edge[:x])
		
		#Defining a list of two lists
		#One for Out and 1 for In
		if a not in Edges.keys():
			Edges[a] = [[],[],0]
		
		temp = ''
		
		for i in range(x+3,len(edge)+1):
			#If the last char or a comma
			if i == len(edge) or edge[i] == ',':
				
				b = int(temp)
				Edges[a][Out].append(b)
				
				if b not in Edges.keys():
					Edges[b] = [[],[],0]
				
				Edges[b][In].append(a)
				temp = ''
			else:
				temp += edge[i]
Graph.close()

for node,edge in Edges.items():
	#For every non 1-1 node
	if isNodeOneToOne(node) == False:
		if len(edge[Out]) > 0:
			edge[Visited] = 1
			for nextNode in edge[Out]:
				temp = []
				#Adding first Node
				temp.append(node)
				temp.append(nextNode)
				tmpNode = nextNode
				Edges[tmpNode][Visited] = 1
				#Continue loop till 1-1 node is there
				while isNodeOneToOne(tmpNode) == True:
					tmpNode = Edges[tmpNode][Out][0]
					temp.append(tmpNode)
					Edges[tmpNode][Visited] = 1
				Paths.append(temp)

#Yet to do isolated cycle
for node,edge in Edges.items():
	#For every 1-1 node
	if isNodeOneToOne(node) == True:
		if edge[Visited] == 0:
			edge[Visited] = 1
			temp = []
			temp.append(node)
			nextNode = edge[Out][0]

			while nextNode != node and Edges[nextNode][Visited] == 0 and isNodeOneToOne(nextNode) == True:
				temp.append(nextNode)
				Edges[nextNode][Visited] = 1
				nextNode = Edges[nextNode][Out][0]

			if nextNode == node:
				temp.append(nextNode)
				Paths.append(temp)

for path in Paths:
	for i in range(len(path)):
		if i == len(path) - 1:
			print(path[i],sep="")
		else:
			print(path[i]," -> ",sep="",end="")