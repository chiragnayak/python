print('-' * 75)

# Simple IF ... ELSE
num = 12

if num % 5 == 0:
    print('S1')
    print('S2')
    print('S3')
else:
    print('S4')
    print('S5')

print('-' * 75)

# Multilevel IF ... ELSE (Alternative to Switch Case Statements)
num = 1

if num % 5 == 0:
    print('Div By 5')
elif num % 3 == 0:
    print('Div By 3')
elif num % 2 == 0:
    print('Div By 2')
else:
    print("Not Div By 2, 3 and 5")

print('-' * 75)

# Nested IF ... ELSE
num = 12

if num % 5 == 0:
    print('Div By 5')

    if num % 3 == 0:
        print('Div By 3')

        if num % 2 == 0:
            print('Div By 2')
        else:
            print('Not Div By 2')
    else:
        print('Not Div By 3')
else:
    print('Not Div By 5')

print('-' * 75)

# Single Line IF ELSE (Conditional/Ternary Operator)
string = 'python'
'''
is_palin = 'No'
if string == string[::-1]:
    is_palin = 'Yes'
'''
is_palin = 'Yes' if string == string[::-1] else 'No'
print('Is Palin -', is_palin)

print('-' * 75)

is_palin = print('Yes') if string == string[::-1] else print('No')
print('Is Palin -', is_palin)

print('-' * 75)

# Loops
# for .. else => based on a collection of values (iterable objects)
# while .. else => based on a condition

# for .. else with strings
for elem in 'python':
    if elem == 't':
        break              # Terminates the Loop
    print('Element -', elem)
else:
    print('For Loop Done')

print('-' * 75)

for elem in 'python':
    if elem == 't':
        break
    print('Element -', elem)

print('For Loop Done')

print('-' * 75)

# for .. else with strings
for elem in 'python':
    if elem == 't':
        continue              # skips the rest of the statements and continues with the next iteration
    print('Element -', elem)
else:
    print('For Loop Done')

print('-' * 75)

# Iterate through the numbers
'''
range => Used to iterate through the numbers
range(6) => 0, 1, 2, 3, 4, 5
range(1, 6) => 1, 2, 3, 4, 5
range(1, 6, 2) => 1, 3, 5
'''
for num in range(10, 5, -1):
    print(num, '-', type(num))

print('-' * 75)

# Taking the range of values
range_num = list(range(1, 6))
print(range_num, '-', type(range_num))

print('-' * 75)

# while ... else
num = 10
while num > 5:
    print('Num using WHILE -', num)
    num -= 1
else:
    print('While Loop Done')

print('-' * 75)
