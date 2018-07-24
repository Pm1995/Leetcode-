#Max Non Negative Subarray
A=[1, 2, 5, -7, 2, 3]
list=[]
temp=[]
for i in range(len(A)):
	if A[i]>0:
		temp.append(A[i])
	elif A[i]<0:
		temp=[]
		continue
	list.append(temp)
new=[]
for j in range(len(list)):
	if list[j] not in new:
		new.append(list[j])

max=0
ans=0
for m in range(len(new)):
	if sum(new[m])>max:
		max=sum(new[m])
		ans=new[m]
		continue
print(ans)
print("\r")

#return Anti Diagonals from Matrix 
