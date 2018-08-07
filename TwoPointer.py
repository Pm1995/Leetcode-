#Given a sorted array A, having N integers. You need to find any pair(i,j) having sum as given number X.
array=[1,3,5,7]
target=12
i=0
j=len(array)-1
while i<j:
	if array[i]+array[j]==target:
		print([array[i],array[j]])
		break
	elif array[i]+array[j]<target:
		i=i+1
	elif array[i]+array[j]>target:
		j=j-1
print("\r")


#Given two sorted arrays A and B, each having length N and M respectively. 
#Form a new sorted merged array having values of both the arrays in sorted format.
nums1=[1,2,3,99]
nums2=[2,5,6,14,15]
a=0
b=0
new=[]

while a<len(nums1) or b<len(nums2):
	if a<len(nums1) and b<len(nums2):
		if nums1[a]<nums2[b]:
			new.append(nums1[a])
			a=a+1
		elif nums1[a]>nums2[b]:
			new.append(nums2[b])
			b=b+1
		elif nums1[a]==nums2[b]:
			new.append(nums1[a])
			new.append(nums2[b])
			a=a+1
			b=b+1
	elif a<len(nums1):
		new=new+nums1[a:]
		a=len(nums1)
	elif b<len(nums2):
		new=new+nums2[b:]
		b=len(nums2)
print(new)
print("\r")

