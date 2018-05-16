
#############################
#
#
#  Funtion 1
#
#
#############################

def printCheckLength(anyString) :

	length = len(anyString)
		
	# if assert condition is true, it will print the message and won't thriw the exception
	# if assert condition is fale, it will throw an exception and any further statements thereafter will not be executed
	#assert(length==0), "Length of String is Zero, How Come?? "
		
	#print ("After assert is present");
		
	return length
	
# Function definition is here
def changeme( refrence, byReference):
  
	if byReference:
		refrence.append([1,2,3,4])
	else:
		refrence = [1,2,3,4]
		
	print ("Values inside the function: ", refrence)
	
	return
	

