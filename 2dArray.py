#sum elements
array=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
sum=0
for i in range(len(array)):
	for j in range(len(array[i])):
		sum=sum+array[i][j]
print(sum)
print("\r")


#print even 
array=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
elements=[]
for i in range(len(array)):
	for j in range(len(array)):
		if array[i][j]%2==0:
			elements.append(array[i][j])
print(elements)
print("\r")


#matrix to heaven
array=[[1,2,3],[4,5,6]]

#1 2 3        
#4 5 6

opt=[]
for i in range(len(array)):
	opt.append(array[0][i])
	print(opt)
print("\r")


opt2=[]
opt3=[]
for i in range(len(array)):
	for j in range(len(array)-1):
		opt2.append(array[i][0])
		opt3.append(array[i][1:3])
		print(opt2,opt3)
print("\r")



#zeros are heros
array=[[1,2,3,0],[5,6,0,8],[9,0,11,12],[13,0,0,16]]
count=0
elements=[]
for i in range(len(array)):
	for j in range(len(array[i])):
		elements.append(array[i][j])
for k in range(len(elements)):
	if elements[k]==0:
		count=count+1
print(count)
print("\r")

#add up to matrices
array1=[[3,6,9],[1,2,3],[4,7,8]]
array2=[[1,2,3],[4,5,6],[7,8,9]]
#array3=[[],[],[]]
#print(array3)
#array3= [[]*3]*3
#print(array3) 

n = 3
m = 3
array3 = [] * n
for i in range(n):
    array3[i] = [ ] * m
print(array3)


for i in range(len(array1[0])):
	sum=array1[0][i]+array2[0][i]
	array3[0].append(sum)

for i in range(len(array1[1])):
	sum=array1[1][i]+array2[1][i]
	array3[1].append(sum)

for i in range(len(array1[2])):
	sum=array1[2][i]+array2[2][i]
	array3[2].append(sum)
print(array3)



#count odd
array=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
count=0
for i in range(len(array)):
	for k in range(len(array[i])):
		if array[i][k]%2!=0:
			count=count+1
print(count)





