"""
#rotate by 90 degree
#import numpy as np
lists=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#newlists=np.empty([4,4])
newlists=[]
for i in range(len(lists)):
	c=[]
	for j in range(len(lists[i])):
		#newlists[i][j]=lists[len(lists)-1-j][i]
		c.append(lists[len(lists)-1-j][i])
	newlists.append(c)
print(newlists)
#print("\r")
#yui=np.array(lists)
"""

"""
#toeplitz matrix
array=[[6,7,8,9,2],[4,6,7,8,9],[1,4,6,7,8],[0,1,4,6,7]]
#array=np.array(array)
print(array)
list=[1]
for i in range(len(array)-1):
	for j in range(len(array[i])-1):
		if array[i][j]!=array[i+1][j+1]:
			list.append(0)
if len(list)==1:
	print(1)
else:
	print(-1)		
print("\r")	

"""
"""
#sum of 2d arrays
list1=[[3,6,9],[1,2,3],[4,7,8]]
list2=[[1,2,3],[4,5,6],[7,8,9]]
new= []

for i in range(len(list1)):
	c = []
	for j in range(len(list1[i])):
		c.append(list1[i][j]+list2[i][j])
	new.append(c)

print(new)
print("\r")

"""

#largest square house
array=[[1,1,1,0,0],[1,1,1,0,0],[0,1,0,1,0],[0,0,1,1,1]]

for i in range(len(array)):
	for j in range(len(array[i])):
		if array[i][j]==0 and i==0:
			print(i,j)

