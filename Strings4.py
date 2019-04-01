
#Given a word, you need to judge whether the usage of capitals in it is right or not.
#We define the usage of capitals in a word to be right when one of the following cases holds:
#All letters in this word are capitals, like "USA".
#All letters in this word are not capitals, like "leetcode".
#Only the first letter in this word is capital if it has more than one letter, like "Google".
#Otherwise, we define that this word doesn't use capitals in a right way.

word="FlaG"

for i in range(2,len(word)):
	if word[0].islower() and word[1].isupper():
		print("false")
	if word[0].isupper() and word[1].isupper():
		if word[i].isupper():
			continue
		else:
			print("false")
	if word[0].islower() and word[1].islower():
		if word[i].islower():
			continue
		else:
			print("false")
	if word[0].isupper() and word[1].islower():
		if word[i].islower():
			continue
		else:
			print("false")

print("\r")


#A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
#We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
S="I speak Goat Latin"

temp=S.split()

ref=["a","e","i","o","u","A","E","I","O","U"]

s=""

for m in range(len(temp)):
	if temp[m][0] in ref:
		temp[m]=temp[m]+"ma" +"a"*(m+1)
	else:
		temp[m]=temp[m][1:] + temp[m][0] + "mat" +"a"*(m+1)

	
for i in temp:
	s=s+ " " + i

print(s[1:])
print("\r")


#
a="aba"
b="cdc"

count=-1
if a not in b:
	count=max(count,len(a))

if b not in a :
	count=max(count,len(b))

print(count)
print("\r")


#X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - 
#we cannot choose to leave it alone.
#A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 
#rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
ref=["2","5","6","9","1","8","0"]
neg_ref=["3","4","7"]

ref=set(ref)
neg_ref=set(neg_ref)


count=0
N=857

for i in range(1,N+1):
	if ("2" in str(i) or "5" in str(i) or "6" in str(i) or "9" in str(i)) and ("3" not in str(i) and "4" not in str(i) and "7" not in str(i)):
		count=count+1

print(count)
print("\r")




#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
s="bcbb"

di={}

for i in s:
	if i not in di:
		di[i]=1
	else:
		di[i]+=1

for m in range(len(s)):
	if di[s[m]]==1:
		print(m)
		break
print("\r")



#You are given a string representing an attendance record for a student. The record only contains the following three characters:
#'A' : Absent.
#'L' : Late.
#'P' : Present.
#A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#You need to return whether the student could be rewarded according to his 

s="PPALLP"

count_A=0

for i in range(len(s)):
	if s[i]=="A":
		count_A+=1
		if count_A==2:
			print("false")
			break
	elif s[i]=="L" and i<=len(s)-3:
		if s[i+1]=="L" and s[i+2]=="L":
			print("false")
			break
print("\r")





#Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
#You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
s="abab"
check=(s*2)[1:-1]
print(s in check)
print("\r")


#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.
dic={"]":"[",")":"(","}":"{"}
stack=[]

s="(("

for i in s:
	if i in dic.values():
		stack.append(i)
	else:
		if len(stack)==0 or dic[i]!=stack.pop(-1):
			print("false")

if len(stack)>0:
	print("false")
else:
	print("true")

print("\r")


#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string ""
strs=["flower","flow","flight"]

mini=min(strs)
maxi=max(strs)



for i,n in enumerate(mini):
	if n!=maxi[i]:
		print(mini[:i])
		break
print("\r")



#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
s= "A man, a plan, a canal: Panama"
s="".join(e for e in s if e.isalnum())
s=s.lower()


for i in range(len(s)//2):
	if s[i]!=s[-(i+1)]:
		print("false")
print("\r")



#Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
#For example, with A = "abcd" and B = "cdabcdab".
#Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
A="abc"
B="cabcabca"

frac=len(B)//len(A)

for i in range(1,frac+3):
	if B in A*i:
		print("true")
print("\r")


#Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
#If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
#then reverse the first k characters and left the other as original.

s = "abcdefg"
k = 3

for i in range(0,len(s),2*k):
	s=(s.replace(s[i:i+k],s[i:i+k][::-1]))

print(s)
print("\r")


