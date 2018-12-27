#Remove Duplicates from Sorted Array
nums = [0,0,1,1,1,2,2,3,3,4]

i=0
while i<len(nums)-1:
	if nums[i]==nums[i+1]:
		nums.pop(i)
	else:
		i=i+1
print(len(nums))
print("\r")


#Merge Sorted Array 
nums1 = [1,2,3,9,10]
nums2 = [2,3,5,6,10,12]


a=0
while a<len(nums1):
	if nums1[a]==0:
		nums1.pop(a)
	else:
		a=a+1


i=0
j=0
while i<len(nums1)-1 and j<len(nums2)-1:
	if nums1[i]<nums2[j]:
		i=i+1
	if nums1[i]>nums2[j]:
		nums1.insert(i,nums2[j])
		nums2.pop(j)
	if nums1[i]==nums2[j]:
		nums1.insert(i,nums2[j])
		nums2.pop(j)



while j<len(nums2):
	nums1.append(nums2[j])
	nums2.pop(j)

print(nums1)
print("\r")



#two sum 

nums = [2, 7, 11, 15]
target = 9
dic={}

for i,n in enumerate(nums):
	m=target-n
	if m in dic:
		print(dic[m],i)
	else:
		dic[n]=i
print("\r")


#Print true if contains duplicates else print false 
num=[1,1,1,3,3,4,3,2,4,2]
d={}


for i in num:
	if i in d:
		print("true")
		break
	else:
		d[i]=0
print("\r")



#
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m=3
n=3

i=0
j=0
while i<m and j<n:
	if nums1[i]>=nums2[j]:
		nums1.insert(i,nums2[j])
		nums2.pop(j)
		i=i+1
	if nums1[i]<nums2[j]:
		i=i+1

while j<len(nums2):
	nums1.insert(i+1,nums2[j])
	#nums1.append(nums2[j])
	nums2.pop(j)
	i=i+1

print(nums1)
print("\r")



nums=[3,2,3]
dic={}

for n in nums:
	if n not in dic:
		dic[n]=1
	else:
		dic[n]=dic[n]+1


for i in dic:
	if dic[i]>len(nums)/2:
		print("true")


