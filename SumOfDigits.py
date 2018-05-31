#give the sume of digits

#enter number here 
nums=2019

#method 1 
sum=0
for i in str(nums):
	sum=sum+int(i)
print(sum)




#method 2 
sum=0
while nums>0:
	sum=sum+nums%10
	nums=nums//10
print(sum)
