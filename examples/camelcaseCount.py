


def camelcaseCount(val):
	#create empty list
	myList = list([])
	#add all strings into it
	for i in list(range(len(val))) :
		myList.append(val[i])
	
	currIndex=0
	count=1
	while True:
		if myList[currIndex].isupper()
			count=count+1
		currIndex=currIndex+1
		if currIndex > len(val)
			break
	
	return count
	

print(camelcaseCount("chiragNayakVariable"))
	
