#queue

def queues(comm,list,elem):
	if comm==1:
		list.append(elem)
	elif comm==2:
		list.pop(0)
	else:
		return list[0]


li=[]
queues(1,li,5)
queues(1,li,6)
print(queues(3,li,6))
queues(2,li,6)
print(queues(3,li,6))
print("\r")




#reverse about a point
list=[1,2,3,4,5,6,7,8]
elem=4
empt=[]
for i in range(list.index(elem)-1,-1,-1):
	empt.append(list[i])
empt.append(elem)
for i in range(len(list)-1,list.index(elem),-1):
	empt.append(list[i])
print(empt)
print("\r")




	
