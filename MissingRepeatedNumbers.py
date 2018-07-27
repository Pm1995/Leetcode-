#Find All Numbers Disappeared in an Array
list=[4,3,2,7,7,2,3,1]
dic={}
for i in range(len(list)):
	dic[list[i]]=0
new=[]
n=len(list)
for i in range(1,n+1):
	if i not in dic:
		new.append(i)
print(new)
print("\r")

#Find All Numbers Disappeared in an Array in 0(1) time
list=[4,3,2,7,8,2,3,1]
for i in range(len(list)):
	index=abs(list[i])-1
	list[index]=-abs(list[index])
new=[]
for i in range(len(list)):
	if list[i]>0:
		new.append(i+1)
print(new)


#N/3 repeat number 
A=[1,2,3,1,1]
