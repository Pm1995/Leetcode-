obs='abcdefghijklmnopqrstuvwxyz'

for i in range(0,5):
	s=""
	for j in range(0,5):
		s=s+obs[j]
	print(s)
print("\r")


for i in range(5,0,-1):
	s=""
	for j in range(0,5):
		s=s+str(i)
	print(s)
print("\r")


for i in range(0,5):
	s=""
	for j in range(5,0,-1):
		s=s+str(j)
	print(s)
print("\r")


for i in range(0,5):
	s=""
	for j in range(0,i+1):
		s=s+"*"
	print(s)
print("\r")


for i in range(5,0,-1):
	s=""
	for j in range(i,0,-1):
		s=s+ "*"
	print(s)
print("\r")



obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,5):
	s=""
	for j in range(0,i+1):
		s=s+obs[i]
	print(s)
print("\r")





obs='abcdefghijklmnopqrstuvwxyz'
for i in range(4,-1,-1):
	s=""
	for j in range(0,5):
		s=s+obs[i]
	print(s)
print("\r")




for i in range(1,5+1):
	s=""
	for j in range(5+1-i,0,-1):
		s=s+str(i)
	print(s)
print("\r")



obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,5):
	s=""
	for j in range(i+1):
		s=s+str(obs[i])
	print(s)
print("\r")






for i in range(0,3):
	s=""
	s="0"*(2-i)
	s=s + "*"*(i+1)
	print(s)
	print("\r")


#problem 24(difficult turn)
n=5
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+"*"*(i+1)
	print(s)
print("\r")




#problem 27
obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+ str(obs[i])*(i+1)
	print(s)
print("\r")



#problem 34
n=5
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+"*"*(2*i+1)
	print(s)
print("\r")


#problem 35
n=5
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+str(i+1)*(2*i+1)
	print(s)
print("\r")




#
obs="abcdefghijklmnopqrstuvwxyz"
n=5
for i in range(0,n):
	s=" "*(i)
	s=s+"*"*(n-1-i)
	#s=s+str(obs[::-23])*(n-1-i)
	print(s)
print("\r")




#problem 38 
obs="abcdefghijklmnopqrstuvwxyz"
n=4
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+str(obs[2*i])*(2*i+1)
	print(s)
print("\r")



#problem 12
for i in range(1,6):
	s=""
	for j in range(1,i+1):
		s=s+str(j)
	print(s)
print("\r")


#problem 19
obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,5):
	s=""
	for j in range(5-i,0,-1):
		s=s+str(obs[5-i-j])
	print(s)
print("\r")




#problem 26
n=5
for i in range(0,n):
	s=" "*(n-i-1)
	for j in range(1,i+2):
		s=s+str(j)
	print(s)
print("\r")


#problem 28 
obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,n):
	s=" "*(n-i-1)
	for j in range(0,i+1):
		s=s+str(obs[j])
	print(s)
print("\r")



#problem 31
n=5
for i in range(0,n):
	s=" "*i
	for j in range(1,n + 1-i):
		s=s+str(j)
	print(s)
print("\r")


#problem 33
obs="abcdefghijklmnopqrstuvwxyz"
n=5
for i in range(0,n):
	s=" "*i
	for j in range(0,n-i):
		s=s+str(obs[j])
	print(s)
print("\r")


#problem 32
n=5
for i in range(0,n):
	s=""
	s=" "*(i)
	s=s+str(obs[n-i-1])*(n-i)
	print(s)
print("\r")


#problem 23 ( continue     )
n=5
for i in range(0,n):
	s=""
	s=s+"*"*(n-i)
	print(s)
print("\r")

obs="abcdefghijklmnopqrstuvwxyz"



#problem 48 
n=5
for i in range(0,n):
	s=" "*(i)
	s=s+str(n-i)*(2*(n-i)-1)
	print(s)
print("\r")


obs='abcdefghijklmnopqrstuvwxyz'

for i in range(0,5):
	s=""
	for j in range(0,5):
		s=s+obs[j]
	print(s)
print("\r")


for i in range(5,0,-1):
	s=""
	for j in range(0,5):
		s=s+str(i)
	print(s)
print("\r")


for i in range(0,5):
	s=""
	for j in range(5,0,-1):
		s=s+str(j)
	print(s)
print("\r")


for i in range(0,5):
	s=""
	for j in range(0,i+1):
		s=s+"*"
	print(s)
print("\r")


for i in range(5,0,-1):
	s=""
	for j in range(i,0,-1):
		s=s+ "*"
	print(s)
print("\r")



obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,5):
	s=""
	for j in range(0,i+1):
		s=s+obs[i]
	print(s)
print("\r")





obs='abcdefghijklmnopqrstuvwxyz'
for i in range(4,-1,-1):
	s=""
	for j in range(0,5):
		s=s+obs[i]
	print(s)
print("\r")




for i in range(1,5+1):
	s=""
	for j in range(5+1-i,0,-1):
		s=s+str(i)
	print(s)
print("\r")



obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,5):
	s=""
	for j in range(i+1):
		s=s+str(obs[i])
	print(s)
print("\r")






for i in range(0,3):
	s=""
	s="0"*(2-i)
	s=s + "*"*(i+1)
	print(s)
	print("\r")


#problem 24(difficult turn)
n=5
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+"*"*(i+1)
	print(s)
print("\r")




#problem 27
obs="abcdefghijklmnopqrstuvwxyz"
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+ str(obs[i])*(i+1)
	print(s)
print("\r")



#problem 34
n=5
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+"*"*(2*i+1)
	print(s)
print("\r")


#problem 35
n=5
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+str(i+1)*(2*i+1)
	print(s)
print("\r")




#
obs="abcdefghijklmnopqrstuvwxyz"
n=5
for i in range(0,n):
	s=" "*(i)
	s=s+"*"*(n-1-i)
	#s=s+str(obs[::-23])*(n-1-i)
	print(s)
print("\r")




#problem 38 
obs="abcdefghijklmnopqrstuvwxyz"
n=4
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+str(obs[2*i])*(2*i+1)
	print(s)
print("\r")






