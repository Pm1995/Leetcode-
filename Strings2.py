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


#Repeated Substring Patterns
#Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together
s="ababba"


ss = (s*2)[1:-1]

print(s in ss)
print("\n")


#repeated string pattern
#Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

A = "a"
B = "aa"

thresh=len(B)//len(A)
flag=0
ans=0

for i in range(1,thresh+2):
	if B in (A*i):
		flag=1
		ans=i
		print(ans)
		break
print("\r")



#March 2019 starts here 

#Given a string, you need to reverse the order of characters in each word within a sentence while 
#still preserving whitespace and initial word order.
s="Let's take LeetCode contest"
news=[]

for j in s.split():
	print(j[::-1])
print("\r")



#Write a function that reverses a string. The input string is given as an array of characters char[].
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
s=["h","e","l","l","o"]
for i in range(len(s)//2):
	s[i],s[-(i+1)]=s[-(i+1)],s[i]
print(s)
print("\r")


#You have an array of logs.  Each log is a space delimited string of words.
#For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#Each word after the identifier will consist only of lowercase letters, or;
#Each word after the identifier will consist only of digits.
#We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
#Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
#Return the final order of the logs.

logs=["qi ir oo i", "cp vnzw i", "0 fkbikbts", "4 j trouka", "gn j q al", "5r w wgqc", "m8 x haje", "fg 28694 6", "i gf mwdoa", "ao 0850716"]

lis_al=[]
lis_dig=[]


for i in logs:
	if i.split()[1].isdigit():
		lis_dig.append(i)
	else:
		lis_al.append(i)


lis_al=sorted(lis_al,key=lambda x:x.split()[1:])
lis_al.extend(lis_dig)
print(lis_al)
print("\r")


