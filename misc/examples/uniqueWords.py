

fhandle = open (input("Enter File To Fetch unique Words : "), encoding="utf8")

uniqueWords = []
for line in fhandle : 
	words = line.split()
	if len(words) == 0 : continue
	for word in words :
		if word in uniqueWords : 
			continue
		else :
			uniqueWords.append(word)
			print ("Unique word %s found ! " % word)

print ("Number of unique words : %d " % len(uniqueWords))
print ("Unique Words : ", uniqueWords)
		