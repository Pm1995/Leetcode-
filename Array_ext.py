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

