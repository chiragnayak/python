print('-' * 75)

# Set => Collection of unique elements enclosed in {}
# Set is unordered and is not indexed
set_elem = {'php', 'python', 'php', 'python', 'perl'}
print(set_elem, '-', type(set_elem))

# Add Elements to the set
set_elem.add('python')
set_elem.add('ruby')
print('After Add -', set_elem)

# Remove Elements from set
rem = set_elem.pop()
print('Removed -', rem)
rem = set_elem.pop()
print('Removed -', rem)
print('After Pop -', set_elem)

print('-' * 75)

lst_a = ['php', 'perl', 'php', 'perl', 'python']
lst_b = ['python', 'ruby', 'shell', 'ruby', 'shell']

print('List A -', lst_a)
print('List B -', lst_b)

set_a = set(lst_a)
set_b = set(lst_b)

print('Set A -', set_a)
print('Set B -', set_b)

# Union => Combining 2 sets after removing duplicates
print('Union -', set_a.union(set_b))

# Intersection => Extracting only the common elements
print('Intersection -', set_a.intersection(set_b))

# Difference A - B => Elements only in A; but not in B
print('Difference A - B -', list(set_a.difference(set_b)))

# Difference B - A => Elements only in B; but not in A
print('Difference B - A -', set_b.difference(set_a))

# Symmetric Difference => Elements that are present only in A and only in B
#                         Elements that are not common to A and B
print('Symm. Diff -', set_a.symmetric_difference(set_b))

print('-' * 75)
