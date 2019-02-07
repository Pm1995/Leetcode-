#remove duplicates from sorted array
nums=[0,0,1,1,1,2,2,3,3,4]
c=0
while c<len(nums)-1:
	if nums[c]==nums[c+1]:
		nums.pop(c)
	else:
		c=c+1


print(nums)
print("\r")


#remove zeroes and then append it in the end 
nums=[0,0,1]
list=[]
for i in nums[:]:
	if i==0:
		list.append(i)
		nums.remove(i)
for k in list:
	nums.append(k)

print(nums)
print("\r")


#longest continuos increasing subsequence
array=[1]
list=[]
cont=[]
count=0
for i in range(len(array)-1):
	if array[i]<array[i+1]:
		count=count+1
		cont.append(count+1)
	else:
		list.append(count+1)
		count=0
		continue

if len(list)>0 and len(cont)>0:
	print(max(max(list),max(cont)))
elif len(array)==1:
	print(1)
elif len(list)==0 and len(cont)==0:
	print(0)
elif len(list)==0 and len(cont)>0:
	print(max(cont))
elif len(list)>0 and len(cont)==0:
	print(max(list))
print("\r")


#Best Time to Buy and Sell Stock
prices=[3,3]
prices.reverse()
list=[]
for i in range(len(prices)):
	start=prices[i]
	for j in range(len(prices)-(i+1)):
		#print(start,prices[j+(i+1)])
		list.append(start-prices[j+(i+1)])
if max(list)>0:
	print(max(list))
else:
	print(0)
print("\r")



#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
nums=[2, 7, 11, 15]
target=9
nums=[2,7,11,15]
target=9
dic={}

for i,n in enumerate(nums):
	m=target-n
	if m not in dic:
		dic[n]=i
	else:
		print([dic[m]+1,i+1])
print("\r")


#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
inp=[0,1,3]

k=len(inp)

sumk=int(k/2*(2*1+(k-1)))

suminp=sum(inp)

if sumk!=suminp:
	print(sumk-suminp)
print("\r")


#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

nums1=[1,2]
nums2=[3,4]
median=0

m=len(nums1)
n=len(nums2)

i=0
j=0
while i<m and j<n:
	if nums1[i]<nums2[j]:
		i=i+1
	elif nums2[j]<=nums1[i]:
		nums1.insert(i,nums2[j])
		nums2.pop(j)
		i=i+1

k=0
while k<len(nums2):
	nums1.append(nums2[k])
	nums2.pop(k)
frac=len(nums1)//2

if len(nums1)%2==0:
	median=(nums1[frac-1] + nums1[frac])/2
else:
	median=nums1[frac]

print(median)
print("\r")


#Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.

array=[1,3,5,6]
target=7
not_found=1

for i,n in enumerate(array):
	if n==target:
		print(i)
		print("yes")
		not_found=0
	elif min(array)>target:
		array.insert(0,target)
		print(array.index(target))
		not_found=0
		break
	elif max(array)<target:
		array.append(target)
		print(array.index(target))
		not_found=0
		break



if not_found==1:
	for i,n in enumerate(array):
		if n>target:
			array.insert(i,target)
			print(i)
			break
print("\r")




#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element 
#in the array contain a single digit.

lis=[1,2,3]
s=""
for i in lis:
	s=s+str(i)

num=0
num=1 + int(s)
li2=[]
for j in str(num):
	li2.append(int(j))

print(li2)
print("\r")


#Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
nums = [0,1,2,2,3,0,4,2]
val = 2


i=0
while i<len(nums):
	if nums[i]==val:
		nums.pop(i)
	else:
		i=i+1

print(nums) 
print("\r")



#max subarray
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
nums=[-2,1,-3,4,-1,2,1,-5,4]

max_so_far=0
max_ending_here=0


for i in range(len(nums)):
	max_ending_here=max_ending_here + nums[i]
	if max_ending_here<0:
		max_ending_here=0
	if max_so_far<max_ending_here:
		max_so_far=max_ending_here

if max_so_far>0:
	print(max_so_far)
else:
	print(max(nums))
print("\r")

