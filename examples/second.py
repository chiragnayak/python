import random
from enum import Enum # to import and use ENUM

random.seed(100)

for i in range(1):
	# for real numbers
	print("For uniform : %.5f" % random.uniform(10,20)) ## Return the next random floating point number in the range [10.0, 20.0).
	print("For random : " ,  random.random()) ## Return the next random floating point number in the range [0.0, 1.0).
	## for integers
	print("For integer, randint (start, stop) : ", random.randint(1,10)) 
	print("For integer, randrange (start, stop[, step]) : ", random.randrange(1,10)) # randrange(start, step [,step]), step is optional, default is 1
	print("For integer, randrange (start, stop, step) : ", random.randrange(0,10,2)) # randrange(start, step, [step])
	print("For integer, randrange (stop) : ",random.randrange(10)) # randrange (stop)
	## for choice
	print ("For choice ", random.choice(list(range(10))));
	## for shuffle
	newList = [1,2,3,4,5,6];
	print ("For Shuffle ", random.shuffle(newList));  # Shuffle the sequence x in place. Python API methods that alter a structure in-place generally return None, not the modified data structure.
	## for sample
	print ("For Sample sample(list/population, sample-size) : ", random.sample(newList, len(newList)))
	print ("For Sample sample(list/population, sample-size) : ", random.sample(range(100), 5))
	print ("++++++++++ EXLORE Real-valued distributions ++++++++ triangular, betavariate, expovariate ++++++++")

#list index starst from '0'
print (list(range(10))) #Prints list of 0 to 10 index, step of 1 [0,1,2,3,4,5,6,7,8,9]	
print (list(range(10))[0:10]) #Prints list of 0 to 10, from 0 to 10th index, step of 1 [0,1,2,3,4,5,6,7,8,9]	
print (list(range(10))[0:7]) #Prints list of 0 to 10, from 0 to 7th index, step of 1 [0,1,2,3,4,5,6]	
print (list(range(10))[0:20]) # out of range access seem to look like no effect here, it will still print up to 10th index only.
print (list(range(5,10))[0:10]) # Starts with five, upto 10, so only 5,6,7,8,9,, i.e. 0th to 4th index, accessing beyond has no effect.
print (list(range(0,40,5))) # in steps of 5, starting from 0 upto 40


##################### ENUMS #########################

class color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3

def printMe(color):
	print("Color is : ", color)
	print("Color repr value is : ", repr(color))
		
for x in color :
	printMe(x)
	print ("name : ", x.name)
	print ("value : ", x.value)
	
print (color['RED'])
print (color['GREEN'])
print (isinstance(color.GREEN, color))

x = input("Enter color : ");

if x == color.RED.name or int(x) == color.RED.value:   # x == color.RED.value will not work because the value is internally int
	print ("COLOR is RED")
else :
	print ("COLOR IS NOT RED, RETRY !!")