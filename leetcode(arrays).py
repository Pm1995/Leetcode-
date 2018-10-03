
"""
#contain duplicates-Given an array of integers, find if the array contains any duplicates.
nums=[1,2,3,1]
dict={}
for i in range(len(nums)):
	dict[nums[i]]=0

for i in nums:
	if i in dict:
		dict[i]=dict[i]+1
list=[]
for i in dict:
	if dict[i]>1:
		print('True')
		break
	else:
		continue
		print('False')
print("\r")



#majority element-Given an array of size n, find the majority element. The majority element is the element 
#that appears more than ⌊ n/2 ⌋ times.
nums=[3,2,3]
dict={}
for i in range(len(nums)):
	dict[nums[i]]=0

for i in nums:
	if i in dict:
		dict[i]=dict[i]+1
for i in dict:
	if dict[i]>len(nums)/2:
		print(i)
print("\r")



#find numbers disappeared in array-Find all the elements of [1, n] inclusive that do not appear in this array.
nums=[4,3,2,7,8,2,3,1]
dict={}
for i in range(len(nums)):
	dict[nums[i]]=0
list=[]
for k in range(max(nums)+1):
	if k not in dict.keys() and k>0:
		list.append(k)
if len(list)>0:
	print(list)
print("\r")


#Given an array of integers that is already sorted in ascending order, find two numbers such that 
#they add up to a specific target number.
nums=[2,7,11,15]
target = 5


list=[]
for i in range(len(nums)):
	start=nums[i]
	for j in range(len(nums)-(i+1)):
		if start+nums[j+i+1]==target:
			#print(start,nums[j+1+i])
			list.append(i+1)
			list.append(j+i+2)

if len(list)>0:
	print(list)
print("\r")



#Given a matrix A, return the transpose of A.
matrix=[[1,2,3],[4,5,6]]
list=[]
for i in range(len(matrix[0])):
	trans=[]
	for j in range(len(matrix)):
		trans.append(matrix[j][i])
	list.append(trans)
print(list)
print("\r")


"""

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

"""
#Third maximum number
array=[3, 2, 1]

largest=array[0]
for i in range(len(array)):
	if largest<array[i]:
		largest=array[i]
array.pop(array.index(largest))

seclarg=array[0]
for i in range(len(array)):
	if seclarg<array[i]:
		seclarg=array[i]
array.pop(array.index(seclarg))
print(array)

"""


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


#roman to integer
ref={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
str='III'
"""
list=[]
for i in str:
	list.append(ref[i])
print(sum(list))
"""

str2="IV"
list2=[]
for i in range(len(str2)):
	if i-1=="I":
		print(str2[i])


for i in range(2,5+1,1):
	if i%2!=0:
		print(i)
print("\r")


#valid palindrome
s="A man, a plan, a canal: Panama"
s=s.lower()
s=''.join(e for e in s if e.isalnum())



for i in range(0,len(s)//2,1):
	if s[i]==s[-(i+1)]:
		print("true")
	else:
		print("False")
print("\r")

#alid Anagram
s = "aacc"
t = "ccac"

dic={}
for i in range(len(s)):
	dic[s[i]]=0




for i in range(len(s)):
	dic[s[i]]+=1


for j in t:
	if j in dic:
		dic[j]=dic[j]-1
	else:
		dic[j]=1000


for i in dic:
	if dic[i]<0:
		dic[i]=1000


if sum(dic.values())==0:
	print("true")
else:
	print("false")