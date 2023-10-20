print('-' * 75)

print('Arithmetic')

print('Add -', 5 + 3)
print('Sub -', 5 - 3)
print('Mul -', 5 * 3)
print('Div -', 5 / 3)
print('Mod -', 5 % 3)
print('FlD -', 5 // 3)
print('Exp -', 5 ** 3)

print('-' * 75)

print('Assignment (Shorthand)')

# =, +=, -=, *=, /=, %=, //=, **=
count = 5
count **= 2        # count = count ** 2
print('count -', count)

print('-' * 75)

print('Comparison')

# ==, !=, >, <, >=, <=
print('Is python greater than php -', 'python' > 'php')
print('Is php greater than perl -', 'php' > 'perl')
print('ASCII VALUE OF E -', ord('E'))
print('Character of 108 -', chr(108))

print('-' * 75)

print('Logical')

# and => True when all the conditions are True
# or => True when any of the given conditions are True
# not => Inverts the result of the boolean expression
string = '1221'
print('Logical -', len(string) % 2 != 0 or string == string[::-1])

print('-' * 75)

print('Membership - in, not in')

# Check whether the given object is the member of another object
string = 'python'
print('Is on present in python -', 'on' in string)

print('-' * 75)

print('Identity - is, is not')

num = len(string)
print(num, '-', type(num))
print('Is num holding int value -', type(num) is int)

num1 = (1, 5)
num2 = (1, 5)

print('num1 -', num1, '-', id(num1))
print('num2 -', num2, '-', id(num2))

print('Both num1 and num2 contains same values -', num1 == num2)
print('Both num1 and num2 contains same references -', num1 is num2)

print('-' * 75)

print('Concatenation : +')

# Data type of all the operands should be same
# If data type is int => addition
# If data type is non-int => concatenation
print('Addition -', 5 + 3)
print('Concat Str -', '5' + '3')
print('Concat List -', [1, 2] + [3])

print('-' * 75)

print('Repetition : *')

# Any one operand type should be non-int; rest should be int
print('Rep 1 -', '5' * 3)
print('Rep 2 -', [[1, 5]] * 3)
print("Rep 3 -", 2 * '3' * 5)

print('-' * 75)

string = '5'
print(string, '-', id(string))

rep_string = string * 3
print(rep_string, '-', id(rep_string), '-', id(rep_string[0]))

string = '6'
print(string, '-', id(string))
print(rep_string, '-', id(rep_string), '-', id(rep_string[0]))

print('-' * 75)
