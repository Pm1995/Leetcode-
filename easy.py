nums=[3,6,1,0]
output=1
check=max(nums)
index=nums.index(check)
print(index)
#nums.remove(check)

list=[]

for i in range(len(nums)):
	if check>=2*nums[i]:
		list.append(1)
	else:
		list.append(-1)

if -1 in list:
	print(-1)
else:
	print(1)