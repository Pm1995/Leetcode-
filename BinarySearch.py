#Two Sum 
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


#Peak index in array 
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



#Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.
#
nums=[1,3,6,9]
target=9

low=0
high=len(nums)-1

while low<=high:
	mid=(low+high)//2
	if target==nums[mid]:
		print(mid)
		break
	elif nums[mid-1]<target and nums[mid]>target:
		print(mid)
		break
	elif nums[mid]<target and nums[mid+1]>=target:
		print(mid+1)
		break
	elif nums[mid]<target:
		low=mid + 1 
	else:
		high=mid-1
print("\r")




#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

x=56
n=0
while n*n<x:
	n=n+1


high=n
low=n-1


if high*high==x:
	print(high)
else:
	print(int(((high-low)/(high*high-low*low))*(x-low*low) + low))

print("\r")



#Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
#find the smallest element in the list that is larger than the given target.
#Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

letters=["c", "f", "j"]
target="a"
flag=0
for i in range(len(letters)):
	if letters[i]<=target:
		continue
	else:
		flag=1
		print(letters[i])
		break

if flag==0:
	print(letters[0])
print("\r")





#square root of integer method 2 using binary search 
n=17

low=0
high=n

while low<=high:
	mid=(low+high)//2
	if mid*mid==n:
		print(mid)
		break
	if mid*mid>n:
		high=mid-1
	else:
		low=mid+1

if mid*mid!=n:
	print(int(((low-high)/(low*low-high*high))*(n-high*high) + high))

print("\r")

