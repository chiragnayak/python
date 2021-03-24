print('-' * 75)

# Regular Expressions => Pattern Matching

import re

# Function to check the pattern
def chk_pattern(inp_pattern, inp_string):
    if re.search(inp_pattern, inp_string, re.I):
        print(inp_pattern, inp_string, 'Satisfied', sep=' -- ')
    else:
        print(inp_pattern, inp_string, 'Not Satisfied', sep=' -- ')

# Get the input from the user
string = input('Enter Any String - ')

print('-' * 75)

# A simple match
chk_pattern('python', string)              # 'python' in string

print('-' * 75)

# Anchors
# ^ - startswith; $ - endswith
chk_pattern('^python', string)
chk_pattern('python$', string)
chk_pattern('^$', string)
chk_pattern('^python$', string)

print('-' * 75)

# Range of characters - []
# [0-9]; [a-z]; [A-Z]; [0-9a-zA-Z]; [1a&%#]
# Group of characters - ()
chk_pattern('^[0-9][_&*](abcd)$', string)
chk_pattern('^[0-9][_&*]abcd$', string)

print('-' * 75)

# Metacharacters (Repetition Cases)
# * => Matches zero to many occ. of previous character or previous group of characters
# + => Matches one to many occ.
# ? => Matches zero or one occ.
chk_pattern('^ab+c$', string)
chk_pattern('^ab*c$', string)
chk_pattern('^ab?c$', string)

chk_pattern('^(ab)+c$', string)
chk_pattern('^(ab)*c$', string)
chk_pattern('^(ab)?c$', string)

print('-' * 75)

# Quantifiers - {}
chk_pattern('^(ab){2}c$', string)        # Exactly 2 occurrences
chk_pattern('^(ab){1,3}c$', string)      # Min 1; Max 3
chk_pattern('^(ab){,3}c$', string)       # Min 0; Max 3
chk_pattern('^(ab){3,}c$', string)       # Min 3; Max 'n'

print('-' * 75)

# Choices - |
chk_pattern('^p(hp|erl|ython)$', string)

print('-' * 75)

# Alternatives - [^]
chk_pattern('^a[0-9]b$', string)
chk_pattern('^a[^0-9]b$', string)

print('-' * 75)

# Dot character - .
chk_pattern('^a.b$', string)
chk_pattern('^python.*script$', string)

print('-' * 75)

# Character range escape sequences
# \d => [0-9]                  ; \D => [^\d]
# \w => [0-9a-zA-Z_]           ; \W => [^\w]
# \s => space, tab or newline  ; \S => [^\s]
chk_pattern(r'^[6-9]\d{9}$', string)

print('-' * 75)

# Search => Looks for the pattern anywhere in the string
searched = re.search(r'\d{3}', string)
if searched:
    print('Searched -', searched)

# Match => Looks for the pattern only at the beginning of the string
matched = re.match(r'\d{3}', string)
if matched:
    print('Matched -', matched)

# Findall => finds all the occurrences of the pattern in the string
print('All Occurrences -', re.findall(r'\d{3}', string))

print('-' * 75)

# Groupings
pattern = '^python (.*) and (.*) script$'
searched = re.search(pattern, string)
if searched:
    print('All groups -', searched.groups())
    print('Group 1 -', searched.group(1))
    print('Group 2 -', searched.group(2))

print('-' * 75)

# Searching for the particular word
string = "python,script,is,on"
print('Finding on -', re.findall('on', string))
print('Finding the word on -', re.findall(r'\bon\b', string))

print('-' * 75)


