#max consecutive gap
array=[1]
array.sort()
list=[]
for i in range(len(array)-1):
	list.append(array[i+1]-array[i])
if len(list)==0:
	print(0)
else:
	print(max(list))
print("\r")


#Wave array
list=[1, 2, 3, 4,5,6,7]
emp=[]
for i in range(len(list)//2):
	emp.append(list[2*i:2*i+2])
for i in range(len(emp)):
	emp[i][0],emp[i][1]=emp[i][1],emp[i][0]
#print(sum(emp, []))
new=sum(emp, [])
if len(list)%2!=0:
	new.append(list[-1])
print(new)
print("\r")


#Maximum distance
array=[3,5,4,2]
list=[]
for i in range(len(array)):
	for j in range(i+1,len(array),1):
		ref=array[i]
		if ref<array[j]:
			list.append(j-i)
print(max(list))
print("\r")


#Maximum distance using efficiency 
array=[3,5,4,2,10]
mydict={}
for i in range(len(array)):
	mydict[array[i]]=i
print(mydict)
trans=[]
for key in sorted(mydict):
	trans.append(mydict[key])
print(trans)

mid=len(array)//2
if len(array)%2==0:
	print(max(trans[mid:]))
else:
	print(max(trans[mid+1:]))
print("\r")

#Find duplicates in subarray 
array=[3,4,1,4,1]
array.sort()
for i in range(len(array)-1):
	if array[i]==array[i+1]:
		print(array[i])
print("\r")



