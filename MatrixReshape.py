nums=[[1,2],[3,4],[5,6]]


trans=[]
for i in nums:
	for t in i:
		trans.append(t)

print(trans)


r=2
c=3

new=[]
for i in range(0,r):
	k =[]
	for j in range(0,c):
		print("iteration no. and index for trans", j)
		print("value to be added",trans[j])
		k.append(trans[j])

		trans.pop(trans[j])
		print('the current list is', trans)

	new.append(k)		



