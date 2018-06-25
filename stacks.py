#reverse string 
word='abcde'
list=[]
newlist=[]

for i in word:
	list.append(i)
for k in range(len(list)):
	newlist.append(list.pop())
s=""
for m in range(len(newlist)):
	s=s+str(newlist[m])
print(s)
print("\r")


#reverse number
num=12345
num=str(12345)
s=""
for i in num[::-1]:
	s=s+i
print(s)
print("\r")


#maximum element
list=[]
def input(com,element,list):
	if com==1:
		list.append(element)
	elif com==2:
		list.pop()
	elif com==3:
		return(max(list))

input(1,97,list)
input(2,97,list)
input(1,20,list)
input(2,20,list)
input(1,26,list)
input(1,20,list)
input(2,20,list)
print(input(3,20,list))
input(1,91,list)
print(input(3,91,list))
print("\r")



#reference
opening='('
def ifbalance(parentheses):
	stack=[]
	for paren in parentheses:
		if paren==opening:
			stack.append(paren)
		else:
			if len(stack)!=0:
				stack.pop()
			else:
				return False
	return len(stack)==0

print(ifbalance(')(()'))


