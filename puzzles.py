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


