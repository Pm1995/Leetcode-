#
numbers = [2,3,4]
target = 6

d={}

for i,n in enumerate(numbers):
	m=target-n
	if n not in d:
		d[m]=i
	else:
		print(i,d[n])
print("\r")


#
A=[0,2,1,0]

max_=-1000000
max_so_far=0

for i in range(len(A)):
	if A[i]>max_:
		max_=A[i]
		max_so_far=max(max_so_far,max_)

print(A.index(max_so_far))
print("\r")


#Given a sorted (in ascending order) integer array nums of n elements and a target value,
#write a function to search target in nums. If target exists, then return its index, otherwise return -1.
nums = [-1,0,3,5,9,12]
target = 9

low=0
high=len(nums)-1

while low<=high:
	mid=(low+high)//2
	if nums[mid]==target:
		print(mid)
		break
	elif nums[mid]<target:
		low=mid+1
	else:
		high=mid-1
print("\r")


#
nums=[1,3]
target=2

low=0
high=len(nums)

while low<high:
	mid=(low+high)//2
	if nums[mid]==target:
		print(mid)
		break
	if nums[mid]<target:
		low=mid + 1 
		if low==high:
			print(high+1)
	if nums[mid]>target:
		high=mid-1
		if low==high and target>nums[low]:
			print(low+1)
		else:
			print(low)

print("\r")


#Given two arrays, write a function to compute their intersection.
nums1=[4,9,5]
nums2=[9,4,9,8,4]

li=[]

k=set(nums1)
m=set(nums2)

if len(k)>=len(m):
	for i in k:
		if i in m:
			li.append(i)
else:
	for i in m:
		if i in k:
			li.append(i)

print(li)
print("\r")

#intersection of arrays
#Each element in the result should appear as many times as it shows in both arrays.
#The result can be in any order.
nums1=[1,3,3,1]
nums2=[1,1,1,3]

di1={}
di2={}

li=[]

for i in range(len(nums1)):
	if nums1[i] not in di1:
		di1[nums1[i]]=1
	else:
		di1[nums1[i]]+=1


for i in range(len(nums2)):
	if nums2[i] not in di2:
		di2[nums2[i]]=1
	else:
		di2[nums2[i]]+=1


for m in di1:
	if m in di2:
		li.extend([m]*min(di1[m],di2[m]))   #use extend which will append an entire list to existing list 

print(li)
print("\r")


"""#
letters = ["e","e","e","e","e","e","n","n","n","n"]
target = "e"

low=0
high=len(letters)-1

while low<high:
	mid=(low+high)//2
	if letters[mid]>target:
		if letters[mid-1]>target:
			high=mid-1
		else:
			print(letters[mid])
			break
	elif letters[mid]<target:
		if letters[mid+1]<=target:
			low=mid+1
		else:
			print(letters[mid+1])
			break

"""