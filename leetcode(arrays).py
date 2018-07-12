
"""
#contain duplicates-Given an array of integers, find if the array contains any duplicates.
nums=[1,2,3,1]
dict={}
for i in range(len(nums)):
	dict[nums[i]]=0

for i in nums:
	if i in dict:
		dict[i]=dict[i]+1
list=[]
for i in dict:
	if dict[i]>1:
		print('True')
		break
	else:
		continue
		print('False')
print("\r")



#majority element-Given an array of size n, find the majority element. The majority element is the element 
#that appears more than ⌊ n/2 ⌋ times.
nums=[3,2,3]
dict={}
for i in range(len(nums)):
	dict[nums[i]]=0

for i in nums:
	if i in dict:
		dict[i]=dict[i]+1
for i in dict:
	if dict[i]>len(nums)/2:
		print(i)
print("\r")



#find numbers disappeared in array-Find all the elements of [1, n] inclusive that do not appear in this array.
nums=[4,3,2,7,8,2,3,1]
dict={}
for i in range(len(nums)):
	dict[nums[i]]=0
list=[]
for k in range(max(nums)+1):
	if k not in dict.keys() and k>0:
		list.append(k)
if len(list)>0:
	print(list)
print("\r")


#Given an array of integers that is already sorted in ascending order, find two numbers such that 
#they add up to a specific target number.
nums=[2,7,11,15]
target = 5


list=[]
for i in range(len(nums)):
	start=nums[i]
	for j in range(len(nums)-(i+1)):
		if start+nums[j+i+1]==target:
			#print(start,nums[j+1+i])
			list.append(i+1)
			list.append(j+i+2)

if len(list)>0:
	print(list)
print("\r")



#Given a matrix A, return the transpose of A.
matrix=[[1,2,3],[4,5,6]]
list=[]
for i in range(len(matrix[0])):
	trans=[]
	for j in range(len(matrix)):
		trans.append(matrix[j][i])
	list.append(trans)
print(list)
print("\r")


"""

#remove duplicates from sorted array
nums=[0,0,1,1,1,2,2,3,3,4]

dict={}
for i in range(len(nums)):
	dict[nums[i]]=0
list=[]
for k in dict.keys():
	list.append(k)
print(list)
print("\r")

"""
#Third maximum number
array=[3, 2, 1]

largest=array[0]
for i in range(len(array)):
	if largest<array[i]:
		largest=array[i]
array.pop(array.index(largest))

seclarg=array[0]
for i in range(len(array)):
	if seclarg<array[i]:
		seclarg=array[i]
array.pop(array.index(seclarg))
print(array)

"""


#remove zeroes
nums=[0,0,1]
#nums=[0,1,0,3,12]

list=[]


for i in nums[:]:
	if i==0:
		list.append(i)
		nums.remove(i)
print(list)


for k in list:
	nums.append(k)

print(nums)

