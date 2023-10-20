ml_line = """this is multiline string
line 2
line 3
"""

print(ml_line)

print(id(ml_line))

print(id(ml_line) == id(ml_line))

"""
string indexing :
left to right : 0, 1, 2, ...
Right to left : -1, -2, -3 ...

slicing:
start index is include
end index is excluded

Single colon cases: string[start_index : end_index]

:n -> first n elements
-n: -> last n elements


[1:-1] valid
[-1:] valid
[:-1] valid
[-1:-13] valid but will still print only -1 th position letter as 
it has to go from left to right by rule 

default value for start index : 0
default value for end index : length of string [but this value can be as high as possible, but it will consider 
only length of string]

cannot go from right to left 
always slices from left to right

with step index:
start_index : end_index : step_inxed

step_index +ve : left to right
step_index -ve : right to left [check start index should be greater that end index]
 - tip : convert first in java for loop and then convert in : : format, that will be easier

[0:6:2] valied 'pto'
[::] valid , complete string
[::-1] reverse string

slicing with or without step index works for :
 - string
 - list
 - tuple

"""
my_string = "python script"
print(my_string[:1])
print(my_string[:-1])
print(my_string[-1:])
print(my_string[4::-2])

"""
operators
"""
print("ASCII Value of A ", ord('A'))
print("Character rep by 108", chr(108))

"""

num1 == num2 => checks for values
num1 is num2 => checks for references

num1 = 5
num2 = 5

num1 == num2 #true
num1 is num2 #true # only for immutables

num1 = [1,2]
num2 = [1,2]

num1 == num2 #true
num2 is num2 #false # list is immutable

num1 = (1,2)
num2 = (1,2)

num1 == num2 #true
num2 is num2 #true # tuple is mutable

"""

"""
concatenation using + operator

data-types of all the operands should be same.

data type int : addition
data type non-int : concatenation

"""

"""

repetition using *

any one operand type should be non-int, others should be int 

'3' * 3 # 333
3 * 3 * '5' # 555555555
[1,2] * 3  # [1, 2, 1, 2, 1, 2]
[[1,2]]  # [[1,2],[1,2][1,2]]

tip: element in object is repeated, not the object

"""

"""
if-else


for

while

data structures :

list : 
 - collection of values enclosed in [], which belongs to any data type.
 - mutable
 - references in list can be deleted, modified, added
 - order is preserved
 - membership operator : x in list_obj
 
 list.append() : single element at the end of the liost
 list.extend() : list of eleements at the end of the list
 list.insert(index, __object__) : insert at specific index
 
 negative index for insert allowed.. 
 if for insert index didn't existed, it will be added in the last
 
 pop() : removes last element in the list, and returnd to the user
 pop(2) : removes the element at index
 
 remove()
 del()
 clear() 
 
"""

my_list = ["chirag", 'nayak', "is", "a", "good", ["boy", "pune", "chirag"]]

"""

tuple : 

 - collection of values enclosed in (), which belongs to any data type.
 - IM-Mutable
 - references in list CANNOT be deleted, modified, added
 - constant list
 - order is preserved ??
 - membership operator : x in list_obj
"""

"""
dict

 - key value pairs
 
 dict.update()
 dict.pop()
 del keys...
 
 list(dict_obj) will print the keys only
 
 iterate through dictionaries
 
 - iterating thru dict object
 
    for x in dict_obj:
        print x # these will be keys
        
    for x in dict_obj.keys()   
        print x # keys 
        
    for val in dict_obj.values():
        print val # only values
        
    for key, val in dict_obj.items() # returns a list of tuple or list of key,value tuple
        print key, value
        
 - to clear dict
    
    dict_obj.clear()
    
 - by default the dictionary is un-ordered dictionary
 - list and tuple maintain insertion order
 - dict, as there is no indexing, no order is maintained. Hence, unordered colelction. 
 
 - there is another collection by name "ordered dictionary"
 
  
"""

"""
set 

- collection of unique elements enclosed in {}
 
 { "chirag", "nayak", "is", "a", "boy"} # only the values in curly braces.
 
- unordered and is not indexed.
- can have the elements stored in any order
- mutable (you can add elements in a set)
    set_obj.add(something)
- can remove first element with pop(). But, what will become first, you are not sure by design
- 

"""

"""
list comprehension

[expr iteration]
[expr iteration <condition>]

"""

sqr_for_list = [n ** 2 for n in range(1, 11)]
sqr_for_list = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print(sqr_for_list)

strings = ["chirag", "nayak", "good", "boy"]
len_list = [len(elm) for elm in strings if len(elm) >= 5]
print(len_list)

# nested list comprehension
sqr_len = [n ** 2 for n in [len(elm) for elm in strings if len(elm) >= 5]]
print(sqr_len)

"""
set comprehension

{expression iteration <condition>}

"""

# this is set comprehension
sqr_for_set_cpmpre = {n ** 2 for n in range(1, 11)}
print(sqr_for_set_cpmpre)
print(type(sqr_for_set_cpmpre))

"""
dict comprehension

{key:val iteration <condition>}

"""

# this is dict comprehension
strings = ["chirag", "nayak", "good", "boy"]
sqr_for_dict_cpmpre = {n: len(n) for n in strings}
print(sqr_for_dict_cpmpre)
print(type(sqr_for_dict_cpmpre))

"""
req:
[{'c': 1, 'h': 1, 'i': 1, 'r': 1, 'a': 1, 'g': 1}, 
{'n': 1, 'a': 2, 'y': 1, 'k': 1}, 
{'g': 1, 'o': 2, 'd': 1}, 
{'b': 1, 'o': 1, 'y': 1}]
"""
wc = [{char: elm.count(char) for char in elm} for elm in strings]
print(wc)