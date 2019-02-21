#Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which 
#makes sum of min(ai, bi) for all i from 1 to n as large as possible.

nums=[1,4,3,2]
nums.sort()

sumi=0
for i in range(0,len(nums)//2):
	sumi=sumi+min(nums[2*i:2*(i+1)])
print(sumi)
print("\r")


#For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].
#Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
A=[2,1,5]
K=806

st=""
for i in A:
	st=st+str(i)


st=str(int(st)+K)

new=[]

for j in st:
	new.append(int(j))
print(new)
print("\r")



#Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
nums=[1,3,5,4,7]

count=1
maxi=0


for i in range(len(nums)-1):
	if nums[i]<nums[i+1]:
		count=count+1
		maxi=max(maxi,count)
	else:
		count=1
		maxi=max(maxi,count)

print(maxi)
print("\r")


#Given a binary array, find the maximum number of consecutive 1s in this array.
nums=[1,0,1,1,0,1]

maxi=0
count=0

for i in nums:
	if i==1:
		count=count+1
		maxi=max(count,maxi)
	else:
		count=0

print(maxi)
print("\r")


#Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#Find all the elements of [1, n] inclusive that do not appear in this array.
#Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

nums=[4,3,2,7,8,2,3,1]

for i in range(0,len(nums)):
	if nums[abs(nums[i])-1]>0:
		nums[abs(nums[i])-1]=nums[abs(nums[i])-1]*(-1)
	elif nums[abs(nums[i])-1]<0:
		continue

listed=[]
for k in range(len(nums)):
	if nums[k]>0:
		listed.append(k+1)

print(listed)
print("\r")




#An array is monotonic if it is either monotone increasing or monotone decreasing.
#An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#Return true if and only if the given array A is monotonic.

nums=[1,2,2,3]

inc="true"
dec="true"

for i in range(len(nums)-1):
	if nums[i]>nums[i+1]:
		inc="false"
	if nums[i]<nums[i+1]:
		dec="false"


print(inc or dec)
print("\r")


#Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. 
#And you need to output the maximum average value.

#Method 1 
nums=[3,3,4,3,0]

k=3
starts=len(nums)-k+1
count=0
maxm=0
negmax=-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


for i in range(0,starts):
	#print(count)
	count=sum(nums[i:i+k])/k
	if count>maxm:
		maxm=max(maxm,count)
		count=0
	if count<0:
		negmax=max(count,negmax)
		count=0

if maxm>0:
	print(maxm)
else:
	print(negmax)


print("\r")


#Method 2 : 
curr_mean=sum(nums[:k])
max_mean=curr_mean


for i in range(0,len(nums)-k):
	curr_mean=curr_mean-nums[i]
	curr_mean=curr_mean+nums[i+k]

	if curr_mean>max_mean:
		max_mean=curr_mean

print(max_mean/k)
print("\r")




