
proceed = 1

try : 
	dictFile = open(input("Enter the file path to create Keys : "), encoding="utf8")
except Exception :
	print (" FILE OPEN ERROR FROM CODE")
	proceed = 0

if proceed==1 :
	# trigger an empty dictionary
	wordDict = dict()

	count = 0
	for line in dictFile :
		wordKeys = line.split()
		for word in wordKeys :
			#wordDict.update({word : count}) # flavor #1
			wordDict.update(dict([(word , count)])) # flavor #2
			count = count+1

	display = input ("Display Keys and values (0/1) ")
	if display == str(1) :
		print (wordDict)
		print (wordDict.keys())
		print (wordDict.values())

	while True :
		inputStr = input("Enter the key to search : ")
		if inputStr == "exit" :
			break
		else :
			if inputStr in wordDict :
				print ("key is present in dictionary at position : {} ".format(wordDict[inputStr]))
			else :
				print ("Key NOT present in dictionary. Try Again !")
				
	# to count how many times each letter appears in the keys above.		
	letterCount = 0
	display = input ("Display letter count map :  ")
	if display == str(1) :
		countMe = dict()
		for keyStr in wordDict.keys() :
			for c in keyStr :
				if c not in countMe:
					countMe[c] = 1
				else:
					countMe[c] = countMe[c] + 1
		print(countMe)
else :
	print ("ERROR IN OPENING FILE, END PROGRAM")

