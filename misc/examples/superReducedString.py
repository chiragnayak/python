
##x = input("Enter String 1 ")
##y = input("Enter String 2 ")
##z = x+" "+y
##print (str(1))
##print (z)
##print("%s %s" % (x,y))


def super_reduced_string(val):

	prevStrLen = len(val)
	str=val
	while True:
		str = trimMe(str)
		lenStr = len(str)
		if str=="Empty String":
			return str
		elif prevStrLen==lenStr:
			return str
		else :
			prevStrLen=len(str)
		

def trimMe(val):
	#create empty list
	myList = list([])
	#add all strings into it
	for i in list(range(len(val))) :
		myList.append(val[i])
	#print (myList)
	i=0;
	while True:
		if (i+1) >= len(myList):
			break
		else :
			if myList[i]==myList[i+1] :
				myList[i] = ""
				myList[i+1] = ""
				#print(myList)
				i=i+2
			else :
				i=i+1
	
	
	str1 = ''.join(myList)
    
	lenStr = len(str1)
    
	if lenStr==0:
		return "Empty String"
	else:
		return str1

print (super_reduced_string("chiiraag"))
print (super_reduced_string("cchhiirraagg"))
print (super_reduced_string("chiragg"))
print (super_reduced_string("cchiragg"))
print (super_reduced_string("baab"))
