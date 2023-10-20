dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# iteration
n = 0
for val in values:
	n += val
	print(n)

print (dishes.keys())
print (dishes.values())
print (list(keys))
print (list(values))
print("This is a dummy comment to enable git compare")

while True : 
	key = input("Enter Key : ")
	if key == "exit": break
	val = input ("Enter Value : ")
	new_Dic = {key : val}
	dishes.update(new_Dic)
	print ("New Dictionary : ", dishes)