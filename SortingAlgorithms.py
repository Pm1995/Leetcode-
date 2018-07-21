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
