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





#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
#such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
def fibonacci(n):
	cache={}
	def sefib(n):
		if n==0:
			return 0
		if n==1:
			return 1
		elif n in cache:
			return cache[n]
		else:
			cache[n]=sefib(n-1) + sefib(n-2)
			return cache[n]
	return sefib(n)


print(fibonacci(2))
print("\r")


#Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
#followed by all the odd elements of A.
#You may return any answer array that satisfies this condition.

nums=[3,1,2,4]

for i in range(len(nums)):
	if nums[i]%2==0:
		nums.insert(0,nums.pop(i))

print(nums)
print("\r")



#Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
#If it is impossible to form any triangle of non-zero area, return 0.
A=[1,2,1]
A.sort()

maxi=0
maxi_so_far=0

for i in range(len(A)-2):
	if A[i] + A[i+1] > A[i+2]:
		maxi=A[i]+A[i+1]+A[i+2]
		maxi_so_far=max(maxi,maxi_so_far)


print(maxi_so_far)
print("\r")


#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
#design an algorithm to find the maximum profit.
#Note that you cannot sell a stock before you buy one.

prices=[1,2]


min_price=1000000

profit=0
max_profit=0

for i in range(len(prices)):
	if prices[i]<min_price:
		min_price=prices[i]
	elif prices[i] - min_price>profit:
		profit=prices[i]-min_price
		max_profit=max(profit,max_profit)

print(max_profit)
print("\r")


#Say you have an array for which the ith element is the price of a given stock on day i.
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).
#Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

prices=[1,2,3,4,5]
minprice=100000000
profit=0


for i in range(len(prices)):
	if prices[i]<minprice:
		minprice=prices[i]
	elif prices[i]-minprice>0:
		profit= profit + prices[i]-minprice
		minprice=prices[i]


print(profit)
print("\r")


#Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, 
#and B[j] is the size of the j-th bar of candy that Bob has.
#Since they are friends, they would like to exchange one candy bar each so that after the exchange, 
#they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
#Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the 
#size of the candy bar that Bob must exchange.
B=[1,2,5]
A=[2,4]


deficit=abs(sum(A)-sum(B))//2

pos=0
neg=0

if sum(A)>sum(B):
	for i in range(len(A)):
		neg=A[i] - deficit
		if neg in B:
			print(neg+deficit,neg)
elif sum(A)<sum(B):
	for i in range(len(A)):
		pos=A[i] + deficit
		if pos in B:
			print(pos-deficit,pos)

print("\r")