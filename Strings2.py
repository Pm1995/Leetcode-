#Isomorphic Strings
s="paper"
t="title"

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
print("\r")



#Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
s="Let's take LeetCode contest"
temp=[]

for j in s:
	temp.append(j)


news=""
for k in range(len(temp)):
	news=news+temp.pop()


for word in news.split():
	temp.append(word)

news2=""
for m in range(len(temp)):
	news2= news2+ " " + temp.pop()

print(news2[1:])
print("\r")


#Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
#It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
dic={}

for c in "!?',;.": paragraph = paragraph.replace(c, " ")
paragraph=paragraph.lower()


for word in paragraph.split():
	if word not in dic:
		if word not in banned:
			dic[word]=1
	else:
		dic[word]=dic[word] +1
dex=max(dic.values())

for m in dic:
	if dic[m]==dex:
		print(m)
print("\r")


#Given two strings s and t , write a function to determine if t is an anagram of s.
s="aacc"
t="ccac"

di={}
flag=0

for i in s:
	if i not in di:
		di[i]=1
	else:
		di[i]=di[i]+1


for m in t:
	if m in di:
		di[m]=di[m]-1
		if di[m]<0:
			flag=1
	else:
		flag=1


if sum(di.values())==0 and flag==0:
	print("true")
else:
	print("false")
print("\r")



#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
s="a"
li=[]

for i in s.split():
	li.append(i)


print(len(li[-1]))
print("\r")


#Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
s=", , , ,        a, eaefa"

#for c in "!,:;'":s=s.replace(c,"")
listed=[]
for i in s.split():
	listed.append(i)

print(len(listed))
print("\r")


#Student Attendance Record
#A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

s="PPALL"
count_a=0
flag_L=0

for i,n in enumerate(s):
	if n=='A':
		count_a=count_a+1
	elif n=='L' and i<len(s)-2:
		if s[i+1]=='L' and s[i+2]=='L':
			flag_L=1

if count_a>1 or flag_L==1:
	print("false")
else:
	print("true")
print("\r")

