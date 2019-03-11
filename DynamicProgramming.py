#best time to buy stock 
prices=[7,1,5,3,6,4]

min_price=1000000
profit=0

for i in range(len(prices)):
	if prices[i]<min_price:
		min_price=prices[i]
	if prices[i]-min_price>profit:
		profit=max(profit,prices[i]-min_price)


print(profit)
print("\r")



#Maximum sum of subarray 
nums=[-1]

max_=nums[0]
max_so_far=0

for i in range(len(nums)):
	max_=max(nums[i],max_+nums[i])
	max_so_far=max(max_so_far,max_)

print(max_so_far)
print("\r")



#fibonacci sequence using dynamic programming 
n=4

listed=[0]*(n+1)

listed[0]=0
listed[1]=1


for i in range(2,n+1):
	listed[i]=listed[i-1]+listed[i-2]

print(listed[n])
print("\r")


#On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#Once you pay the cost, you can either climb one or two steps. 
#You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
cost = [10,15]

m=len(cost)

listed=[0]*(m+1)

listed[1]=0
listed[0]=0


for i in range(2,m+1):
	listed[i]=min(listed[i-2]+cost[i-2],listed[i-1]+cost[i-1])

print(listed)
print("\r")


#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

n=3
listed=[0]*(n+1)

listed[0]=0
listed[1]=1
listed[2]=2

for i in range(3,n+1):
	listed[i]=listed[i-1]+listed[i-2]

print(listed[n])
print("\r")


#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
#the only constraint stopping you from robbing each of them is that adjacent houses have security system 
#connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
# of money you can rob tonight without alerting the police.

nums=[1,2,3,1]

n=len(nums)
listed=[0]*(n+1)

listed[0]=nums[0]
listed[1]=nums[1]

for i in range(2,n):
	listed[i]=nums[i]+max(listed[:i-1])

print(listed)
print("\r")
