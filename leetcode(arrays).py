#move zeros-Given an array nums, write a function to move all 0's 
#to the end of it while maintaining the relative order of the non-zero elements.

nums=[0,1,0,3,12]



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


