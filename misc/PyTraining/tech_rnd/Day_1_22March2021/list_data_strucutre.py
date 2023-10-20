print('-' * 75)

# List => Collection of values enclosed in [] which belongs to any data type
# List is Mutable => References can be added, modified or deleted

# List of elements
scr_list = ['php', 'perl', 'python', 'shell', 'ruby']
print(scr_list, '-', type(scr_list))

# Use of Membership Operator
print('Is on present in scr_list -', 'on' in scr_list)
print('Is python present in scr_list -', 'python' in scr_list)

# Indexing
print('scr_list[-3] -', scr_list[-3])
print('scr_list[-3:] -', scr_list[-3:])
print('scr_list[-3::-1] -', scr_list[-3::-1])

print('-' * 75)

# Modify the existing references
scr_list[0] = "python"
print('After Modify 1 -', scr_list)

scr_list[1:4] = ['php', 'shell', 'ruby']
print('After Modify 2 -', scr_list)

print('-' * 75)

# Add the elements to the list

# append => always adds the given element to the end of the list
scr_list.append('python')
print('After Append -', scr_list)

# insert => adds the given element to the specified index
scr_list.insert(100, 'ruby')
print('After Insert -', scr_list)

# extend => extends the list by adding more than one elements to the end of the list
other = ['python', 'php', 'python', 'perl']
scr_list.extend(other)
print('After Extend -', scr_list)

scr_list.append(other)
print('After Append -', scr_list)

print('-' * 75)

# Remove the elements from the list

# pop
removed = scr_list.pop()
print('Element Removed -', removed)
print('After Pop 1 -', scr_list)

removed = scr_list.pop(2)
print('Element Removed -', removed)
print('After Pop 2 -', scr_list)

# remove
scr_list.remove('python')
print('After Remove -', scr_list)

while scr_list.count('python'):
    scr_list.remove('python')
else:
    print('After Remove All -', scr_list)

# Del
del scr_list[1:4]          # Remove the indexes 1, 2 and 3
print('After Del -', scr_list)

# Clear
scr_list.clear()
print('After Clear -', scr_list)

print('-' * 75)
