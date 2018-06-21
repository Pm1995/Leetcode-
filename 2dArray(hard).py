#rotate by 90 degree
array=[[1,2,3,4,20],[5,6,7,8,30],[9,10,11,12,40],[13,14,15,16,50],[21,22,23,24,25]]

import numpy as np
lists=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
newlists=np.empty([4,4])
for i in range(len(lists)):
	for j in range(len(lists[i])):
		newlists[i][j]=lists[len(lists)-1-j][i]
print(newlists)
print("\r")
#yui=np.array(lists)



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


