


#Return sorted array from two sorted arrays
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]


i=0
j=0

m=3
n=3


while i<m and j<n:
	if nums1[i]<=nums2[j]:
		i=i+1
	else:
		nums1.insert(i,nums2[j])
		j=j+1


while j<n:
	nums1.insert(i+1,nums2[j])
	i=i+1
	j=j+1

nums1=nums1[:m+n]
print(nums1)
print("\r")


#disjoin to arrays
a=[1,2,3,4,5,6,7,8]
b=[2,4,1]

listed=list(set(a)^set(b))

print(listed)
print("\r")


#Matrix Sums 
matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#row sum
for i in range(len(matrix)):
	summed=0
	for j in range(len(matrix[0])):
		summed=summed+matrix[i][j]
	print(summed)
print("\r")

#column sum

for i in range(len(matrix[0])):
	summ=0
	for j in range(len(matrix)):
		summ=summ+matrix[j][i]
	print(summ)
print("\r")


#Write a function that takes a sentence and prints out the same sentence with each word backwards in O(n) time.
sentance="Hello World"

#print(sentance[::-1])
new=""
for i in sentance.split():
	new=new + " " + i[::-1]

print(new[1:])
print("\r")



#Write a function that prints the least integer that is not present in a given list and cannot be 
#represented by the summation of the sub-elements of the list
array=[1, 2, 3, 4, 5, 6]

res=1
for i in range(len(array)):
	if array[i]<=res:
		res=res+array[i]
	else:
		break
print(res)
print("\r")

#You have a stream of data coming in of size n, but you don’t know what n is ahead of time. 
#Can you write an algorithm that will take a random sample of k elements

import random

stream=[1,2,4,6,9]

k=3

listed=[]


for i in range(0,k):
	s=random.choice(stream)
	stream.remove(s)
	listed.append(s)

print(listed)
print("\r")

