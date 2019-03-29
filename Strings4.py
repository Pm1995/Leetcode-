
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
s="cc"

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

