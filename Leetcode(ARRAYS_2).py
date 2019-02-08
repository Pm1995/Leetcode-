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

