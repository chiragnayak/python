
proceed = 1

def printDict(dictionary) : 
	print ("======= Total : {} entries ========".format(len(dictionary)))
	
	for d in dictionary.keys() :
		print (d, " : ", dictionary[d])
	print ("===================================")

try : 
	dictFile = open(input("Enter the file path to create Keys : "), encoding="utf8")
except Exception :
	print (" FILE OPEN ERROR FROM CODE")
	proceed = 0

if proceed==1 :
	# trigger an empty dictionary
	wordDict = dict({'Mon':0, 'Tue':0,'Wed':0,'Thu':0,'Fri':0,'Sat':0,'Sun':0}) # day basis how many emails
	userDict = dict(); # user basis how many emails
	domCountDic = dict()
	for line in dictFile :
		wordKeys = line.split()
		if "From" in wordKeys :
			#update days count
			wordDict[wordKeys[2]] = int(wordDict[wordKeys[2]]) + 1
			
			#update user count
			if wordKeys[1] not in userDict :
				userDict[wordKeys[1]] = 1
			else : 
				userDict.update(dict([(wordKeys[1] , userDict[wordKeys[1]]+1)]))
			
			#update domain count
			domain = str(wordKeys[1].split('@')[1])
			if domain not in domCountDic :
				domCountDic[domain] = 1
			else : 
				domCountDic.update(dict([(domain , domCountDic[domain]+1)]))
		else :
			print (".")
	printDict (wordDict)
	printDict (userDict)
	printDict (domCountDic)
	
