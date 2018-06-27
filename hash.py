#hash reference
"""
d={}
d['a']=1
d['b']=2
d['c']=3
print(d)

#d[key]=value

print(d['b'])
print("\r")

for i in d.keys():
	print(d[i])
print("\r")

for k,v in d.items():
	print (k,v)
print("\r")


keys=['1','2','3']
value=['a','b','c']

hash={k:v for k,v in zip(keys,value)}
print(hash)
print("\r")

"""
#missing elements
array=[3,1,3,2]
n=4
ref=[]
for i in range(1,n+1,1):
	ref.append(i)

dict={}
for i in range(len(array)):
	dict[array[i]]=0

for i in range(len(ref)):
	if ref[i] not in dict.keys():
		print(ref[i])
print("\r")


#count duplicates
string='abcdeeeeee'

dict={}
for i in string:
	dict[i]=0

for i in string:
	if i in dict.keys():
		dict[i]=dict[i]+1
for k in dict:
	if dict[k]>1:
		print(dict[k])
print("\r")


#remove duplicates
string='abcdeeeeee'
dict={}
for i in string:
	dict[i]=0
emp=''
for j in dict.keys():
	emp=emp + str(j)
print(emp)
print("\r")

#occuring odd times
array=[2,2,3,3,4,4,1,5,5]
dict={}
for i in range(len(array)):
	dict[array[i]]=0
for i in range(len(array)):
	dict[array[i]]=dict[array[i]]+1
for k in dict:
	if dict[k]!=2:
		print(k)
print("\r")


#two non repeating ones
array=[2,2,3,3,4,4,1,5]
dict={}
for i in range(len(array)):
	dict[array[i]]=0

for i in range(len(array)):
	dict[array[i]]=dict[array[i]]+1
count=0
for k in dict:
	if dict[k]==1:
		count=count+k
print(count)