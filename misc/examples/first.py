import funcs

print ("Hi There !!")
print ("[  This is My First Python Program using a text file, hope you like it ! ]")
print ("")
print ("<<<< !! Indentation is very important !! >>>>")

print ("else you might get IndentationError: expected an indented block ")
print ("Basically indentation ends a code block.")
print ("")
print ("Enter a Number :  ")
try :
	x = int(input())
	y = int(input("Enter it again : "))
	
	# Note 'If' syntax, no parenthesis, and followed with a :
	# same holds for 'else', no parenthesis and followed with a :
	if x==y:
		if x>50:
			print ("value is greater than 50")
		elif x==50:
			print ("value is exact 50. Super !!")
			print ("Try again to hit another check !!")
		else :
			print ("value is LESS than 50") ## Note : indentation in next line shifted, this ends the else block. 
		if x%2==0:
			print ("Value is even")
		else :
			print ("Value is ODD")
	else :  # Check use of format. Placing a # is not affecting any thing.
		print ("Two numbers entered are not same #First-Is {} : #Second-Is : {} ".format(x,y))
		print ("Two numbers entered are not same #First-Is %s : #Second-Is : %s" % (x,y))
		raise ("Two numbers are not valid, (thrown via exception)", x,y)
			
except Exception:
	print("except block : Input is incorrect format, Please try again Later !!")
else:
    print ("else block of try : No exception occured, WOW !!") 
finally:
	print ("finally block of try: This is finally block")
	
print (funcs.printCheckLength(str(input("Enter one String : "))))

myList = [10,20,30]
print (myList)
funcs.changeme(myList, True)
print ("Values outside the function: ", myList)
funcs.changeme(myList, False)
print ("Values outside the function: ", myList)
	


