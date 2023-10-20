word = "cha cha1 cha2 cha3 cha4 cha99 cha234"
t = tuple()
t.__add__(tuple(word.split()))
print(t)
t = tuple(word.split())
x = t.__add__(tuple(word.split()))
print(x)
print (t)


#  ---output---
# ()
# ('cha', 'cha1', 'cha2', 'cha3', 'cha4', 'cha99', 'cha234', 'cha', 'cha1', 'cha2', 'cha3', 'cha4', 'cha99', 'cha234')
# ('cha', 'cha1', 'cha2', 'cha3', 'cha4', 'cha99', 'cha234')
#
# Process finished with exit code 0

