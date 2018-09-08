#Given a sorted array A, having N integers. You need to find any pair(i,j) having sum as given number X.
array=[1,3,5,7]
target=12
i=0
j=len(array)-1
while i<j:
	if array[i]+array[j]==target:
		print([array[i],array[j]])
		break
	elif array[i]+array[j]<target:
		i=i+1
	elif array[i]+array[j]>target:
		j=j-1
print("\r")


#Given two sorted arrays A and B, each having length N and M respectively. 
#Form a new sorted merged array having values of both the arrays in sorted format.
nums1=[1,2,3,99]
nums2=[2,5,6,14,15]
a=0
b=0
new=[]

while a<len(nums1) or b<len(nums2):
	if a<len(nums1) and b<len(nums2):
		if nums1[a]<nums2[b]:
			new.append(nums1[a])
			a=a+1
		elif nums1[a]>nums2[b]:
			new.append(nums2[b])
			b=b+1
		elif nums1[a]==nums2[b]:
			new.append(nums1[a])
			new.append(nums2[b])
			a=a+1
			b=b+1
	elif a<len(nums1):
		new=new+nums1[a:]
		a=len(nums1)
	elif b<len(nums2):
		new=new+nums2[b:]
		b=len(nums2)
print(new)
print("\r")


#Given an array having N integers, find the contiguous subarray having sum as great as possible, but not greater than M
array=[-2,1,-3,4,-1,2,1,-5,4]

#method 1:using Kandane's algo 
sum_so_far=0
greatest_so_far=0

for i in range(len(array)):
	sum_so_far=sum_so_far+array[i]
	if sum_so_far<0:
		sum_so_far=0
	if greatest_so_far<sum_so_far:
		greatest_so_far=sum_so_far
print(greatest_so_far)
print("\r")

#method 2: using two pointer 
i=0
j=len(array)-1
new=[]
while i<j:
	new.append(sum(array[i:j+1]))
	if array[i]<array[j]:
		i=i+1
	if array[j]<=array[i]:
		j=j-1

print(max(new))
print("\r")



#merge two sorted arrays
nums=[1,2,3,4,5,6,7]
k=3


while k>0:
	nums.insert(0,nums[-1])
	nums.pop(len(nums)-1)
	k=k-1
print(nums)
print("\r")


#Find First and Last Position of Element in Sorted Array
nums = [1,2,4,5,6,6]
target = 6

list=[]
i=0
while i<=len(nums)-1:
	if nums[i]==target:
		list.append(i)
	i=i+1


if len(list)==0:
	print([-1,-1])
else:
	print([list[0],list[-1]])



#summary ranges
list=[0,1,2,4,5,7]

new=[]
for i in range(len(list)-1):
	temp=[]
	if list[i+1]-list[i]==1:
		temp.append([list[i],list[i+1]])
		new.append(temp)
	else:
		temp=0
		continue
print(new)

print("\r")


#Majority element
nums=[1,1,1,3,3,2,2,2]
dictionary={}
list=[]

for i in range(len(nums)):
	dictionary[nums[i]]=0

for i in range(len(nums)):
	if nums[i] in dictionary:
		dictionary[nums[i]]=dictionary[nums[i]]+1


for i in dictionary:
	if dictionary[i]>len(nums)//3:
		list.append(i)

print(list)
print("\r")