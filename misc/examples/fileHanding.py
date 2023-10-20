
## Dives into basic file handling and related usage cases



try :
	count = 0
	questions1 = 0
	questions2 = 0
	fhand = open(input("Enter the file path : "),encoding="utf8")
	print ("Success !! ", fhand)
	fhandWrite = open(input("Enter the file path to write : "),'w')
	print ("Success !!", fhandWrite)
		
	for line in fhand:
		count = count+1
		# Note : The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator:
		#Approach #1
		if line.find("Q.") != -1 :
			questions1 = questions1 + 1
			print ("> %s " % line)
		#Approach 2
		if "Q." in line:
			questions2 = questions2 + 1
			print ("Copied > %s " % line)
			fhandWrite.write(line)
	
except Exception :
	print ("FILE OPERATION TRIGGERERD ERROR !!")
	

				
print ("Total %d Lines" % (count))
print ("Approach 1 Total %d Questions" % (questions1))
print ("Approach 2 Total %d Questions" % (questions2))