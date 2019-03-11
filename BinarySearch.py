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


#
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

