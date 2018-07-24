#maximum absolute difference
A=[2,2,2]
list=[]
for i in range(len(A)):
	for j in range(len(A)):
		if A[i]>A[j]:
			nums=A[i]-A[j] + i-j
			list.append(nums)
		elif A[i]<A[j]:
			nums=-1*(A[i]-A[j]) + 1*(i-j)
			list.append(nums)
		elif A[i]==A[j]:
			nums=A[i]-A[j] + i-j
			list.append(nums)
print(max(list))
print("\r")


#Missing Number Array
nums=[1,2]
if len(nums)==1 and 1 in nums:
	print(0)
else:
	print(int(abs(len(nums)*(len(nums)+1)/2-sum(nums))))
	print("\r")


#find pivot index
nums = [-1,-1,-1,-1,-1]
def ttt(nums):
	for i in range(len(nums)):
		if sum(nums[:i])==sum(nums[i+1:]):
			return(i)
	return(-1)

print(ttt(nums))
print("\r")


#maximum subarray using Kadane's Algorithm
nums=[-2,-1]
max_ending_here=0
max_so_far=0

for i in range(len(nums)):
	max_ending_here=max_ending_here+nums[i]
	if max_ending_here<0:
		max_ending_here=0
	elif max_so_far<max_ending_here:
		max_so_far=max_ending_here
if max_so_far>0:
	print(max_so_far)
else:
	print(max(nums))