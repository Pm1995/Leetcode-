#Isomorphic Strings
s="paper"
t="title"

if len(s)!=len(t):
	print("false")
dictionart={}
check={}
for i in range(len(s)):
	dictionart[s[i]]=t[i]
for i in dictionart:
	check[dictionart[i]]=0

for i in dictionart.values():
	if i in check.keys():
		check[i]=check[i]+1

count=0
for i in check.values():
	if i>1:
		count=count+1
if count>1 or len(s)!=len(t):
	print("false")
else:
	print("true")

