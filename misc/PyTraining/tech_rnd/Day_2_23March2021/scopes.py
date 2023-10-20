print('-' * 75)

# Scopes => Defines the lifetime of the variable

def change_num():
    global num
    num = 50
    print('In change_num -', num)

def change_num_again():
    global num
    num = 500
    print('In change_num_again -', num)

num = 5
change_num()
print('After change_num -', num)

change_num_again()
print('After change_num_again -', num)

print('-' * 75)

# Function to Change the List
def change_list(lst):
    print('Id of lst -', id(lst))
    lst.extend([4, 5])
    print('In change_list -', lst)

# Pass By Reference
num_list = [1, 2, 3]
print('Id of num_list -', id(num_list))
'''
lst = num_list          # Shallow Copy => Both Ref and Data are copied
'''
change_list(num_list)
print('After change_list -', num_list)

print('-' * 75)

# Pass By Value
num_list = [1, 2, 3]
print('Id of num_list -', id(num_list))
'''
lst = num_list[:]
lst = [1, 2, 3]         # Deep Copy => Only Data is Copied, but not Ref
'''
change_list(num_list[:])
print('After change_list -', num_list)

print('-' * 75)
