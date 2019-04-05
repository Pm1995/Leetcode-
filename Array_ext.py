#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#You may return any answer array that satisfies this condition.
A=[3,1,2,4]
i=0
c=len(A)
c=0
while c<len(A):
	if A[i]%2!=0:
		A.append(A.pop(i))
	else:
		i=i+1
	c=c+1

print(A)
print("\r")



#Move all the zeros to the end in-place
nums=[0,1,0,3,12]

c=len(nums)
c=0
i=0
while c<len(nums):
	if nums[i]==0:
		nums.append(nums.pop(i))
	else:
		i=i+1
	c=c+1

print(nums)
print("\r")


#Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
#Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
A=[0,2,1,-6,6,-7,9,1,2,0,1]

parts=sum(A)//3


count=0
check=0

for i in A:
	count=count+i
	if count==parts:
		check=check+1
		count=0

if check==3:
	print("true")
else:
	print("false")
print("\r")


#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
nums=[3,0,1]

check=(len(nums)*(len(nums)+1))//2

print(check-sum(nums))
print("\r")



#Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#The order of elements can be changed. It doesn't matter what you leave beyond the new length


nums = [0,1,2,2,3,0,4,2]
val = 2


c=0
i=0

k=len(nums)

while c<k:
	if nums[i]==val:
		nums.pop(i)
	else:
		i=i+1
	c=c+1

print(len(nums))
print("\r")


#Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
nums=[1,3,5,4,7,8,9,10,11,12]
count=0
count_so_far=0

for i in range(len(nums)-1):
	if nums[i]<nums[i+1]:
		count=count+1
		count_so_far=max(count,count_so_far)
	else:
		count=0

print(count_so_far+1)
print("\r")



#In a given integer array nums, there is always exactly one largest element.
#Find whether the largest element in the array is at least twice as much as every other number in the array.
#If it is, return the index of the largest element, otherwise return -1.
nums = [3,6,1,0]

maxi=max(nums)

for i in range(len(nums)):
	if nums[i]==maxi:
		continue
	else:
		if nums[i]*2>maxi:
			print("false")

print(nums.index(maxi))
print("\r")


#Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. 
#And you need to output the maximum average value.
nums=[4,2,1,3,3]
k=2


curr=sum(nums[:k])

max_yet=curr

for i in range(len(nums)-k):
	curr=curr-nums[i]+nums[i+k]
	max_yet=max(max_yet,curr)

print(max_yet)
print("\r")





#Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. 
#The time complexity must be in O(n).
nums=[2, 2, 3, 1]


setted=set(nums)
if len(setted)<3:
	print(max(nums))
else:
	print(sorted(setted)[-3])
print("\r")

