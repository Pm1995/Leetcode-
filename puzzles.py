#Happy Number
num=19
ans=num
while ans!=1:
	temp=str(ans)
	ans=0
	for i in temp:
		ans=ans+int(i)**2
	if ans==1:
		print("true")
		break

