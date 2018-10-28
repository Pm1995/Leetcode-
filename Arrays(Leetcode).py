#Two Sum 
nums = [2, 7, 11, 15]

target = 9
dic={}

for i,n in enumerate(nums):
	m=target-n
	dic[m]=i

list=[]
for l in nums:
	if l in dic:
		list.append(dic[l])

print(sorted(list))
print("\r")


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
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

i=0
j=0
while i<m and j<n:
	if nums1[i]<=nums2[j]:
		i=i+1
	if nums1[i]>nums2[j]:
		nums1.insert(i-1,nums2[j])
		nums2.pop(j)

while j<n:
	if nums1[i]<=nums2[j]:
		nums1.append(nums2[j])
		j=j+1


print(nums1)
