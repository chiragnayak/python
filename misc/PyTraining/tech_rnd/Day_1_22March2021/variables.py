print('-' * 75)

# Single Line Comment

'''
Easy to read and  understand => indentation
simple syntax
rich set of libraries

Python is an interpreted language, there is no main function in the program and the execution starts
from the very first line
Python supports both procedural oriented and object-oriented programming
'''

# Variables (Data Structures)
'''
Iterable Objects => Can be iterated and it is indexed
    str, list, tuple, dictionary, set
        Mutable Objects => References can be added, deleted or modified
            list, dictionary and set
        Immutable Objects => References cannot be added, deleted or modified
            str, tuple

Non-Iterable Objects => Cannot be iterated
    int, float, boolean
'''
# Dynamic Typing
var = 1
print(var, '-', type(var))

var = 1.5
print(var, '-', type(var))

var = 'A'
print(var, '-', type(var))

var = "Python"
print(var, '-', type(var))

var = True
print(var, '-', type(var))

print('-' * 75)

# Multi line strings
ml_str_1 = '''Line1
Line2
Line3'''

ml_str_2 = """Line1
Line2
Line3"""

print('ml_str_1 -', ml_str_1)
print('ml_str_2 -', ml_str_2)

print('-' * 75)

# Strings
string = "Python Script"
print('string -', string, '-', id(string))

print('-' * 75)

# Indexing
# From left to right => 0, 1, 2 and so on
# From right to left => -1, -2, -3 and so on
'''
0     1     2     3     4     5     6     7     8     9     10    11    12
P     y     t     h     o     n           S     c     r     i     p     t
-13   -12   -11   -10   -9    -8    -7    -6    -5    -4    -3    -2    -1
'''
print('string[5] -', string[5], '-', id(string[5]))
print('string[-5] -', string[-5], '-', id(string[-5]))

# string[5] = 'N'       # Not possible, as string is immutable object

print('-' * 75)

# Slicing
'''
for(i=0;i < 6; i++)
{
  print(string[i])   # 0, 1, 2, 3, 4, 5
}
'''
# string[si:ei]
# by default, si = 0; ei = len(string)
# 'si' is included and 'ei' is excluded
'''
0     1     2     3     4     5     6     7     8     9     10    11    12
P     y     t     h     o     n           S     c     r     i     p     t
-13   -12   -11   -10   -9    -8    -7    -6    -5    -4    -3    -2    -1
'''
print('string[0:6] -', string[0:6])
print('string[:3] -', string[:3])              # First 'n' elements
print('string[-5:] -', string[-5:])            # Last 'n' elements
print('string[1:-1] -', string[1:-1])
print('string[-13:-1] -', string[-13:-1])
print('string[-13:] -', string[-13:])
print('string[:] -', string[:])                # string[0:13]

print('-' * 75)

'''
for(i=0;i < 6; i+=2)
{
  print(string[i])   # 0, 2, 4
}
'''
# string[si:ei:step_idx]
# By default step_idx => +1
# If step_idx is +ve => goes from left to right
# If step_idx is -ve => goes from right to left, i.e., in the reverse order
print('string[::] -', string[::])           # string[0:13:1]
print('string[::-1] -', string[::-1])

print('string[0:6:2] -', string[0:6:2])     # Pto

'''
for(i=4; i>=0; i-=2)
{
  print(string[i])
}
'''
print('string[0:6:-2] -', string[0:6:-2])
print('string[4::-2] -', string[4::-2])

print('-' * 75)
