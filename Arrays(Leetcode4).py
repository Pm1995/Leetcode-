#In a string S of lowercase letters, these letters form consecutive groups of the same character.
#For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#The final answer should be in lexicographic order.

S="abbxxxxzyyyy"
lis=[]
count=1

for i in range(len(S)-1):
	if S[i]==S[i+1]:
		count=count+1
		if count==len(S) and count>=3:
			lis.append([len(S)-count,len(S)-1])
	else:
		if count>=3:
			lis.append([i-count+1,i])
		count=1


mount=1
for m in range(len(S)-1):
	if S[-(m+1)]==S[-(m+2)]:
		mount=mount+1
	else:
		if mount>=3:
			lis.append([len(S)-mount,len(S)-1])
		mount=1
		break
print(lis)
print("\r")



#Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
#Here a k-diff pair is defined as an integer pair (i, j), where
#i and j are both numbers in the array and their absolute difference is k.
nums=[1,1,1,1,1]
k=0
lis=set()

nums.sort()

d={}

for n in nums:
	if n in d:
		lis.add((n,d[n]))
	d[n+k]=n


		


print(len(lis))
print("\r")



#In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
#There is at least one empty seat, and at least one person sitting.
#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
#Return that maximum distance to closest person.

seats=[1,0,0,0,1,0]


maxi=0
loc=0
leloc=0
temp=0


for i in range(len(seats)):
	if seats[i]==1:
		continue
	else:
		try:
			loc=seats[i:].index(1)
		except:
			loc=10000000000000
		try:
			leloc=seats[:i][::-1].index(1) + 1 
		except:
			leloc=100000000000


		maxi=max(maxi,min(loc,leloc))



print(maxi)
print("\r")


#Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - 
#they would compete for water and both would die.
#Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
#and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
flowerbed=[0,0,1,0,0]

n = 1

lef=0
righ=0
mini=0
count=0


for i in range(len(flowerbed)):

	if flowerbed[i]==1:
		continue
	else:
		try:
			lef=flowerbed[:i][::-1].index(1) + 1
		except:
			lef=1000
		try:
			righ=flowerbed[i:].index(1)
		except:
			righ=1000
		mini=min(lef,righ)

		if mini>1:
			count=count+1
			flowerbed[i]=1


if count==n:
	print("true")
else:
	print("false")
print("\r")




#In a deck of cards, each card has an integer written on it.
#Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
#Each group has exactly X cards.
#All the cards in each group have the same integer.
deck=[0,0,0,0,0,1,1,2,3,4]

d={}
for n in deck:
	if n not in d:
		d[n]=1
	else:
		d[n]=d[n]+1




x=min(d.values())


for i in d.values():
	if i%x==1:
		print("false")

print("\r")




#Given an integer array, you need to find one continuous subarray that if you 
#only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#You need to find the shortest such subarray and output its length.

nums=[2, 6, 4, 8, 10, 9, 15]

m=0
n=0

for i in range(len(nums)-1):
	if nums[i]!=sorted(nums)[i]:
		m=i
		break



for j in range(len(nums))[::-1]:
	if nums[j]!=sorted(nums)[j]:
		n=j
		break


print(n-m+1)
print("\r")


