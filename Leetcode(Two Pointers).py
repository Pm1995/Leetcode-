#Reverse String
s= "A man, a plan, a canal: Panama"
new=""

p=len(s)-1
while p>=0:
	new=new+s[p]
	p=p-1
print(new)
print("\r")


#Move Zeroes
nums=[4,2,4,0,0,3,0,5,1,0]

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


#Two Sum II - Input array is sorted
#Given an array of integers that is already sorted in ascending order, 
#find two numbers such that they add up to a specific target number.

numbers =[2,7,11,15]
target = 9

i=0
j=len(numbers)-1
list=[]

while i<j:
	if numbers[i]+numbers[j]<target:
		i=i+1
	elif numbers[i]+numbers[j]>target:
		j=j-1
	elif numbers[i]+numbers[j]==target:
		list.append((i+1,j+1))
		i=i+1
		j=j-1

print(list)
print("\r")


#Valid Palindrome
s="A man, a plan, a canal: Panama"
s=s.lower()
new=''.join(e for e in s if e.isalnum())

i=0
j=len(new)-1
c=0

while i<j:
	if new[i]!=new[j]:
		print("false")
		break
	elif new[i]==new[j]:
		i=i+1
		j=j-1
		c=c+1
if c*2==len(new) or (c*2)+1==len(new):
	print("true")
print("\r")



#Remove Element-Given an array nums and a value val, remove all instances of that value in-place and return
                #the new length.

nums = [3,2,2,3]
val = 3
i=0

while i<len(nums):
	if nums[i]==val:
		nums.pop(i)
	elif nums[i]!=val:
		i=i+1
print(len(nums))
print("\r")

#Remove duplicates from sorted array 
nums = [0,0,1,1,1,2,2,3,3,4]

i=0
while i<len(nums)-1:
	if nums[i]!=nums[i+1]:
		i=i+1
	else:
		nums.pop(i)
print(nums)
print("\r")




#Merge Sorted Array 
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

i=0
j=0
list=[]

while i<len(nums1) and j<len(nums2):
	if nums1[i]<nums2[j]:
		list.append(nums1[i])
		nums1.pop(i)
	elif nums2[j]<nums1[i]:
		list.append(nums2[j])
		nums2.pop(j)
	elif nums1[i]==nums2[j]:
		list.append(nums1[i])
		nums1.pop(i)
		list.append(nums2[j])
		nums2.pop(j)

while i<len(nums1):
	list.append(nums1[i])
	nums1.pop(i)

		
while j<len(nums2):
	list.append(nums2[j])
	nums2.pop(j)


m=0
while m<len(list)-1:
	if list[m]==0:
		list.pop(m)
	else:
		m=m+1
print(list)

