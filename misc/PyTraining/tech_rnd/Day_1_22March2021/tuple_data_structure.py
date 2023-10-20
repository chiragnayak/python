print('-' * 75)

# Tuple => Collection of values enclosed in () which belongs to any data type
# Tuple is Immutable => References cannot be added, modified or deleted
# Tuples => Constant Lists

# Tuple of elements
scr_tup = ('php', 'perl', 'python', 'shell', 'ruby')
print(scr_tup, '-', type(scr_tup))

# Use of Membership Operator
print('Is on present in scr_tuple -', 'on' in scr_tup)
print('Is python present in scr_tuple -', 'python' in scr_tup)

# Indexing
print('scr_tup[-3] -', scr_tup[-3])
print('scr_tup[-3:] -', scr_tup[-3:])
print('scr_tup[-3::-1] -', scr_tup[-3::-1])

print('-' * 75)
