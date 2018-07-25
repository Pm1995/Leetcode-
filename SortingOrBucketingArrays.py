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