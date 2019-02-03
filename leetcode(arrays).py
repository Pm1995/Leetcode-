#remove duplicates from sorted array
nums=[0,0,1,1,1,2,2,3,3,4]

dict={}
for i in range(len(nums)):
	dict[nums[i]]=0
list=[]
for k in dict.keys():
	list.append(k)
print(list)
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
dicti={}

for i in range(len(nums)):
	#dicti[nums[i]]=0
	m=target-nums[i]
	dicti[nums[i]]=m
list=[]

for d in dicti:
	if d + dicti[d]==9 and dicti[d]>0:
		list.append(d)
		list.append(dicti[d])
		break

for i in range(len(list)):
	print(nums.index(list[i]))
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

