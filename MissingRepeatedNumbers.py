#Find All Numbers Disappeared in an Array
list=[4,3,2,7,7,2,3,1]
dic={}
for i in range(len(list)):
	dic[list[i]]=0
new=[]
n=len(list)
for i in range(1,n+1):
	if i not in dic:
		new.append(i)
print(new)
print("\r")

#Find All Numbers Disappeared in an Array in 0(1) time
list=[4,3,2,7,8,2,3,1]
for i in range(len(list)):
	index=abs(list[i])-1
	list[index]=-abs(list[index])
new=[]
for i in range(len(list)):
	if list[i]>0:
		new.append(i+1)
print(new)
print("\r")

#N/3 repeat number 
A=[1,2,3,1,1]
dict={}
for i in range(len(A)):
	dict[A[i]]=0

for i in range(len(A)):
	dict[A[i]]=dict[A[i]]+1
for k in dict:
	if dict[k]>len(A)/3:
		print(k)
print("\r")

#Contains duplicates
nums=[1,2,1,1]
dict={}
for i in range(len(nums)):
	dict[nums[i]]=0
for j in range(len(nums)):
	dict[nums[j]]=dict[nums[j]]+1
if len(nums)>0:
	print(max(dict.values())>1)
else:
	print(len(nums)==1)
print("\r")


#Contains duplicates 2- Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and 
#the absolute difference between i and j is at most k.
