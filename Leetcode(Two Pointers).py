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

"""
i=0
j=len(nums)-1
while i<=j:
	if nums[i]==0:
		nums.pop(i)
		nums.append(0)
		j=j-1
	if nums[j]==0:
		if j==len(nums)-1:
			j=j-1
		else:
			nums.append(nums[j])
			nums.pop(j)
			i=i+1

	if nums[i]!=0 and nums[j]!=0:
		i=i+1
		j=j-1

print(nums)


"""
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



