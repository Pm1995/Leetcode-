
#
"""
S="I speak Goat Latin"

wovel=["a","e","i","o","u"]

for i in S.split():
	if i[0].lower() in wovel:
		print(i+"ma")
		i=i+"ma"
	else:
		i=i[1:]+i[0]+"ma"

"""


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


