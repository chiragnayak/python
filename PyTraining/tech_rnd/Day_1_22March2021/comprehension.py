print('-' * 75)

# Without using comprehension
sqr = []
for n in range(1, 11):
    if n % 5 == 0 or n % 3 == 0:
        sqr.append(n ** 2)
print('sqr -', sqr)

# List Comprehension
# [expr iteration <condition>]
sqr_lc = [n ** 2 for n in range(1, 11) if n % 5 == 0 or n % 3 == 0]
print('sqr_lc -', sqr_lc)

print('-' * 75)

# List of strings
strings = ['shell', 'perl', 'ruby', 'python', 'c_java']
len_lc = [len(elem) for elem in strings]
print('Len LC -', len_lc)

print('-' * 75)

# List of strings
strings = ['php', '1221', 'perl', 'python', 'madam']
chk_palin_lc = [elem == elem[::-1] for elem in strings]
print('CHK Palin LC -', chk_palin_lc)

palin_lc = [elem for elem in strings if elem == elem[::-1]]
print('Palin LC -', palin_lc)

print('-' * 75)

# Set Comprehension
# {expr iteration <condition>}
strings = ['shell', 'perl', 'ruby', 'python', 'c_java']
len_sc = {len(elem) for elem in strings}
print('Len SC -', len_sc, '-', type(len_sc))

print('-' * 75)

# Dictionary Comprehension
# {key: value iteration <condition>}
strings = ['shell', 'perl', 'ruby', 'python', 'c_java']
len_dc = {elem: len(elem) for elem in strings}
print('Len DC -', len_dc, '-', type(len_dc))

print('-' * 75)

# List of strings
strings = ['php', 'mam']
'''
dc = [{'p': 2, 'h': 1},
      {'m': 2, 'a': 1}]
'''
wc = [{char: elem.count(char) for char in elem} for elem in strings]
print('wc -', wc)

print('-' * 75)
