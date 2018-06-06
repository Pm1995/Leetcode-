#problem 40
n=5
for i in range(0,n):
	s=" "*(n-1-i)
	s=s+"*"*(2*(i+1)-1)
	print(s)


n=5
for i in range(0,n):
	s=" "*(n-1-i)
	for j in range(0,i+1):
		s=s+str(j)
	print(s)
print("\r")


#hard difficulty

#problem 9 
obs="abcdefghijklmnopqrstuvwxyz"
n=5
for i in range(0,n):
	s=""
	s=str(obs[n-1::-1])
	print(s)
print("\r")



#problem 41 
obs="abcdefghijklmnopqrstuvwxyz"
n=5
for i in range(0,n): 
	s=" "*(n-i-1)
	for j in range(0,2*i+1):
		s=s+str(obs[j])
	print(s)
print("\r")





#problem 49
n=5
for i in range(0,n):
	s=""
	for j in range(0,i+1):
		s=" "*i
		s=s+str(2*n-(2*j+1))*(2*(n-i)-1)
	print(s)
print("\r")



