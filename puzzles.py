#Happy Number
num=19
ans=num
while ans!=1:
	temp=str(ans)
	ans=0
	for i in temp:
		ans=ans+int(i)**2
	if ans==1:
		print("true")
		break
print("\r")


#best time to buy and sell stock 
prices=[7,6,4,3,1]
list=[]
for i in range(len(prices)-1):
	if prices[i]>max(prices[i+1:]):
		continue
	if prices[i]<max(prices[i+1:]):
		list.append(max(prices[i+1:])-prices[i])

if len(list)>0:
	print(max(list))
else:
	print(0)
print("\r")



#roman to integer
mydict = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
s="L"
num=0
for i in range(len(s)-1):
	if mydict[s[i]]<mydict[s[i+1]]:
		num=num-mydict[s[i]]
	else:
		num=num+mydict[s[i]]
print(num+mydict[s[-1]])
print("\r")



#happy number
n=19
s=str(n)

ans=n
while ans!=1:
	temp=str(ans)
	ans=0
	for i in temp:
		ans=ans+int(i)*int(i)
	if ans==1:
		print("true")
		break
print("\r")


#first bad version 
n=10
bversion=4
dict={}

for i in range(0,n):
	dict[i+1]=0
	if i+1<bversion:
		dict[i+1]="false"
	if i+1>=bversion:
		dict[i+1]="true"

print(dict[4])
print("\r")



#Add digits until sum==1
num=99

#method 1 
len=1000
while len!=0 and num!=0:
	sum=int(str(num)[0]) + int(str(num)[1])
	len=sum//10
	num=sum

if num!=0:
	print(sum)
else:
	print(0)
print("\r")

#method 2 
while num>9:
	num=sum(int(x) for x in str(num))
print(num)
print("\r")




#Find square root without calculator
thresh=8
root=0
store_b=0

n=0
while n*n<thresh:
	n=n+1
	if n*n>=thresh:
		store_b=n

store_a=store_b-1

if store_b*store_b==thresh:
	root=store_b
else:
	root=store_a + (thresh-store_a*store_a)*(store_b-store_a)/(store_b*store_b-store_a*store_a)

print(root)
print("\r")


