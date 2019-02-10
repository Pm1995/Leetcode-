#Given an array, rotate the array to the right by k steps, where k is non-negative.
nums=[-1,-100,3,99]
k = 2

while k>0:
	nums.insert(0,nums.pop(-1))
	k=k-1

print(nums)
print("\r")


#Given an array of integers and an integer k, find out whether there are two distinct indices i and j in 
#the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
nums = [1,0,1,1]
k = 1
flag=0

d={}

for i,n in enumerate(nums):
	if n not in d:
		d[n]=i
	else:
		if i-d[n]<=k:
			flag=1
		else:
			d[n]=i


if flag==0:
	print("false")
else:
	print("true")
print("\r")


#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
nums=[1]

n=len(nums)

summ=(n*(n+1))//2
if summ!=sum(nums):
	if summ>sum(nums):
		print(summ-sum(nums))
	else:
		print(sum(nums)-summ)

if (summ==1 and n==1) or (summ==sum(nums) and 0 not in nums):
	print("0")
print("\r")



#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#method 1 
nums=[0,1,0,3,12]
i=0
while sum(nums[i:])!=0:
	if nums[i]==0:
		nums.append(0)
		nums.pop(i)
	else:
		i=i+1

print(nums)

#method 2 
nums=[0,1,0,3,12]
c = 0
i=0
while c <len(nums):
	if nums[i]==0:
		nums.pop(i)
		nums.append(0)
	else:
		i=i+1
	c+= 1
print(nums)

print("\r")


#Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, 
#return the maximum number. The time complexity must be in O(n).
nums=[1,2,2,3]
nums.sort()

d={}
i=0
c=1


while i<len(nums)-1:
	if nums[-(i+1)]!=nums[-(i+2)]:
		d[nums[-(i+1)]]=c
		d[nums[-(i+2)]]=c+1
		c=c+1
	else:
		d[nums[-(i+1)]]=c
		d[nums[-(i+2)]]=c
	i=i+1

flag=0
for k in d:
	if d[k]==3:
		print(k)
		flag=1

if flag==0:
	print(max(nums))
print("\r")




#
nums=[4,3,2,7,8,2,3,1]
c=0
nums.sort()
while c<len(nums)-1:
	if nums[c+1]==nums[c]:
		nums.pop(c+1)
	else:
		c=c+1

k=0
v=0
while k<len(nums)-1:
	if nums[v+1]-nums[v]>1:
		nums.insert(v+1,nums[v]+1)
	v=v+1
	k=k+1

print(nums)




