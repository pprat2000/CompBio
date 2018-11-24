#Comp Bio Fall 2018
#Assignment 2, Question 3
#SBU ID : 112027432

#Defining Variables
Edges = {}
Path = list()
Out,In = 0,1
Stack = list()
start,end = -1,-1

#Taking Graph Input
with open("rosalind_ba3g.txt","r") as Graph:
	for edge in Graph:
		edge = edge.strip()

		x = edge.find('-')
		a = int(edge[:x])
		
		#Defining a list of two lists
		#One for Out and 1 for In
		if a not in Edges.keys():
			Edges[a] = [[],[]]
		
		temp = ''
		
		for i in range(x+3,len(edge)+1):
			#If the last char or a comma
			if i == len(edge) or edge[i] == ',':
				
				b = int(temp)
				Edges[a][Out].append(b)
				
				if b not in Edges.keys():
					Edges[b] = [[],[]]
				
				Edges[b][In].append(a)
				temp = ''
			else:
				temp += edge[i]
Graph.close()

#Find start and end node for the path
for node,edge in Edges.items():
	if len(edge[Out]) == len(edge[In]) + 1:
		start = node
	elif len(edge[Out]) + 1 == len(edge[In]):
		end = node

#If all have same in and out degree, selecet any two
if start == -1 and end == -1:
	i = 0
	for node in Edges.keys():
		if i == 0:
			start = node
			i = 1
		elif i == 1:
			end = node
			break

while len(Edges[start][Out]) > 0 or len(Stack) > 0:
		if len(Edges[start][Out]) == 0:
			Path.append(start)
			start = Stack.pop()
		else:
			Stack.append(start)
			temp = Edges[start][Out][len(Edges[start][Out])-1]
			Edges[start][Out] = Edges[start][Out][:-1]
			start = temp
Path.append(start)

print(Path[-1],sep="",end="")
for i in range(len(Path)-2,-1,-1):
	print("->",Path[i],sep="",end="")