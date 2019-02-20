#Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which 
#makes sum of min(ai, bi) for all i from 1 to n as large as possible.

nums=[1,4,3,2]
nums.sort()

sum=0
for i in range(0,len(nums)//2):
	sum=sum+min(nums[2*i:2*(i+1)])
print(sum)
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



#
"""
S = "abbxxxxzyy"

list1=[]
list2=[]

for i in range(len(S)-1):
	if S[i]==S[i+1]:
		list2.append(S[i])
	elif S[i]!=S[i+1] or i+1==len(S)-1:
		list2.append(S[i])
		list1.append(list2)
		list2=[]


#edge case 
for i in range(len(S)-1):
	if S[-(i+1)]==S[-(i+2)]:
		list2.append(S[-(i+1)])
	else:
		list2.append(S[-(i+1)])
		list1.append(list2)
		list2=[]
		break

print(list1)"""



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



