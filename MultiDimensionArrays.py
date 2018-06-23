#longest chain
#part1-get elements from matrix
array=[[3,2,5],[4,1,4],[5,6,5]]
list=[]
dict={}
newl=[]
for i in range(len(array)):
	for j in range(len(array[i])):
		list.append(array[i][j])
		list.sort()
for m in range(len(list)):
	dict[list[m]]=0
for k in dict:
	newl.append(k)

#part2-get maximum sequence 
count=0
list=[]
for i in range(len(newl)-1):
	if newl[i]==newl[i+1]-1:
		count=count+1
	else:
		list.append(count+1)
		count=0
		continue
list.append(count+1)
print(max(list))
print("\r")





#matrix in diagonal order
array=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
for l in range(len(array[0])+len(array)-1):
	list=[]
	for i in range(len(array)):
		for j in range(len(array[i])):
			if i+j==l:
				list.append((array[i][j]))
	list.reverse()
	print(list)
print("\r")


#impact on rows and columns
matrix=[[1,0,0],[0,0,0]]
r=len(matrix)
c=len(matrix[0])


row=[0]*r   #create artificial row and column 
col=[0]*c

for i in range(len(row)):
	for j in range(len(col)):
		if matrix[i][j]==1:
			row[i]=1
			col[i]=1

for i in range(len(row)):
	for j in range(len(col)):
		if row[i]==1 or col[j]==1:
			matrix[i][j]=1
print(matrix)
print("\r")
