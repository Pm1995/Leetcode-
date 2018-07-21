#Insertion Sort
array=[7,2,4,1,5,3]

for i in range(1,len(array),1):
	value=array[i]
	hole=i
	while hole>0 and array[hole-1]>value:
		array[hole]=array[hole-1]
		hole=hole-1
	array[hole]=value
print(array)
print("\r")


#Merge Sort
array=[4,6,3,2,1,5]
def mergesort(list):
	if len(list)>1:
		mid=len(list)//2
		lefthalf=list[:mid]
		righthalf=list[mid:]

		mergesort(lefthalf)
		mergesort(righthalf)

		i=0
		j=0
		k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				list[k]=lefthalf[i]
				i=i+1
			else:
				list[k]=righthalf[j]
				j=j+1
			k=k+1

		while i<len(lefthalf):
			list[k]=lefthalf[i]
			i=i+1
			k=k+1
		while j<len(righthalf):
			list[k]=righthalf[j]
			j=j+1
			k=k+1


mergesort(array)
print(array)
print("\r")


#Quicksort 
array2=[4,6,3,2,1,7,5]
def quicksort(list,start,end):
	if start<end:
		pindex=partition(list,start,end)
		quicksort(list,start,pindex-1)
		quicksort(list,pindex+1,end)

def partition(list,start,end):
	pivot=list[end]
	pindex=start
	for i in range(start,end,1):
		if list[i]<=pivot:
			list[i],list[pindex]=list[pindex],list[i]
			pindex=pindex+1
	list[pindex],list[end]=list[end],list[pindex]
	return pindex

quicksort(array2,0,6)
print(array2)